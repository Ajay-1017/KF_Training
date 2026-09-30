import redis
import time
from database import SessionLocal
from models import ReviewJob
from ai_service import review_code , RetryableError
from storage_service import read_source_code

MAX_ATTEMPTS = 3

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# print(redis_client.connection_pool.connection_kwargs)


def process_job(job_id):
    db = SessionLocal()

    try:
        job = db.get(ReviewJob, int(job_id))

        if job is None:
            print(f"Job {job_id} not found")
            return
        print(f"Processing job {job_id}")

        job.status = "processing"
        job.attempts += 1
        db.commit()

        print(f"Job {job_id} → processing")


        source_code = read_source_code(job.source_location)
        
        findings = review_code(source_code)
        
        job.review_result = str(findings)
        job.status = "completed"

        db.commit()

        # ACK
        redis_client.lrem("processing_queue", 1, job_id)
        redis_client.hdel("processing_jobs", job_id)

        print(f"Job {job_id} → completed")
        print(f"Findings: {findings}")

    except RetryableError as e:
        if job.attempts < MAX_ATTEMPTS:

            delay = 2 ** job.attempts
            
            print(f"Job {job_id} failed: {e}")
            print(f"Waiting {delay} seconds before retrying...")


            redis_client.lrem("processing_queue", 1, job_id)
            redis_client.hdel("processing_jobs", job_id)
            time.sleep(delay)

            job.status = "queued"
            db.commit()

            redis_client.rpush("review_queue", job_id)

            print(f"Job {job_id} failed. Retrying...")

        else:
            job.status = "failed"
            db.commit()
            redis_client.lrem("processing_queue", 1, job_id)
            redis_client.hdel("processing_jobs", job_id)     

            print(f"Job {job_id} failed permanently: {e}")

    except Exception as e:
        job.status = "failed"
        db.commit()

        redis_client.lrem("processing_queue", 1, job_id)
        redis_client.hdel("processing_jobs", job_id)   
        
        print(f"Job {job_id} failed permanently: {e}")

    finally:
        db.close()


def worker():
    print("Worker started. Waiting for jobs...")

    while True:
        
        job_id = redis_client.brpoplpush(
            src = "review_queue",
            dst = "processing_queue",
            timeout = 0
        )

        redis_client.hset(
            "processing_jobs",
            job_id,
            time.time()
        )
        print(f"Received job {job_id}")
        # job_id = result[1]  BLPOP : The return value is a tuple: (list_name, value)
        process_job(job_id)

        
if __name__ == "__main__":
    worker()