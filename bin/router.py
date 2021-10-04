from fastapi import FastAPI

# import routers
from tasks.login import router as login_router
from tasks.register import router as register_router

# add routes here
routes = [
    {
        'prefix': '/user',
        'tags': ['user'],
        'routers': [login_router, register_router]
    }
]


def initiate_routers(app: FastAPI):
    for route in routes:
        for router in route.get('routers'):
            app.include_router(router=router, prefix=route.get(
                'prefix'), tags=route.get('tags'))
