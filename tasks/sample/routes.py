from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SampleSchema(BaseModel):
    sample: str

@router.post("/sample")
async def sample(request: SampleSchema):
    return request
