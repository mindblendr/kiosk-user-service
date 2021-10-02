from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginSchema(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(request: LoginSchema):
    return request
    # return await user_service.login(request.get('username'), request.get('password'))
