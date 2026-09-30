import redis


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


def enqueue_job(job_id):
    redis_client.rpush("review_queue", job_id) # Put the new item at the right/end of the list.