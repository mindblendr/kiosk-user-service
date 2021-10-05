from fastapi.params import Body
from models.user import User
from pydantic import BaseModel
from fastapi import APIRouter
import bcrypt, time, jwt, os
from bin.session_cache import session_cache


# SCHEMA
class LoginSchema(BaseModel):
    username: str
    password: str


# ROUTES
router = APIRouter()


@router.post(path="/login")
async def login(request: LoginSchema = Body(...)):
    user = await User.filter(username=request.username, status=1).get_or_none()
    if user is not None:
        if bcrypt.checkpw(request.password.encode('utf-8'), user.password.encode('utf-8')):
            token = jwt.encode(payload={
                'id': user.id,
                'username': user.username,
                'status': 1,
                'exp': int(time.time()) + int(os.getenv('JWT_TTL'))
            }, key=os.getenv('JWT_SECRET'))

            session_cache_key = str(user.id)
            session_cache.set(key=session_cache_key, payload={
                              'id': user.id, 'username': user.username, 'status': 1}, expire_in_secs=int(os.getenv('JWT_TTL')))

            return {
                'data': {
                    'token': token
                },
                'status': 1
            }
    return {
        'status': 0
    }
