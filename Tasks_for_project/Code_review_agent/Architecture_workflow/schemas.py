from pydantic import BaseModel, ConfigDict


class ReviewRequest(BaseModel):
    source_code: str

class ReviewRequestResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id : int
    status : str
    source_location: str | None



