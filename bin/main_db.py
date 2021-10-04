import os
from fastapi.applications import FastAPI
from tortoise.contrib.fastapi import register_tortoise

models_dir = 'models'
model_files = os.listdir(os.curdir + '/' + models_dir)
models = []
for model_file in model_files:
    if model_file.__contains__('.py'):
        models.append(models_dir.replace('/', '.') + '.' + model_file.replace('.py', ''))

def init_main_db(app: FastAPI):
    register_tortoise(
        app=app,
        db_url=os.getenv('MAINDB_URL'),
        modules={'models': models},
        generate_schemas=True,
        # add_exception_handlers=True,
    )
