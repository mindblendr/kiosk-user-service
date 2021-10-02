from fastapi import FastAPI

# 1. add routers from other services
from .sample.routes import router as sample_router
from .login.routes import router as login_router


def initiate_routers(app: FastAPI):
    # 2. include the router here
    app.include_router(sample_router, prefix='/sample', tags=['sample'])
    app.include_router(login_router, prefix='/user', tags=['user'])