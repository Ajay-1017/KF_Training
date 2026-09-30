from sqlalchemy.orm import Session
from storage_service import save_source_code
from models import ReviewJob


def create_review_job(db: Session , source_code : str):

    job = ReviewJob(
        status="queued",
    )

    db.add(job)
    db.flush()
    
    source_location = save_source_code(
        job.id,
        source_code
    )

    job.source_location = source_location

    db.commit()
    db.refresh(job)

    return job