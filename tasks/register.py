from models.user import User
from pydantic import BaseModel
from fastapi import APIRouter
import bcrypt

# SCHEMA
class RegisterSchema(BaseModel):
    username: str
    password: str

# ROUTES
router = APIRouter()

@router.post(path="/register")
async def register(request: RegisterSchema):
    user = await User.filter(username=request.username).get_or_none()
    if user is None:
        user = User()
        result = await user.create(username=request.username, password=bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'))
        if result:
            return {
                'status': 1
            }
    return {
        'status': 0
    }
