from fastapi import FastAPI , status
from myQueue import enqueue_job
from database import SessionLocal
from job_service import create_review_job
from schemas import ReviewRequest , ReviewRequestResponse

app = FastAPI()


@app.post(
    "/reviews", 
    response_model = ReviewRequestResponse, 
    status_code= status.HTTP_201_CREATED
)

def create_review( request : ReviewRequest):
    db = SessionLocal()

    try:
        job = create_review_job(
            db,
            request.source_code
        )

        enqueue_job(job.id)

        return job
    
    finally:
        db.close()