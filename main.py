from logging import debug
from dotenv import load_dotenv
load_dotenv()
import os
from fastapi import FastAPI
import uvicorn
from tasks.export_routers import initiate_routers

if os.getenv('ENVIRONMENT', 'dev') == 'prod':
    app = FastAPI(debug=False, docs_url=None)
else:
    app = FastAPI(debug=True)

# go to tasks.<SERVICE_NAME> and check router, add routers to ./tasks/export_routers.py
initiate_routers(app)


if __name__ == '__main__':
    uvicorn.run("main:app", port=int(os.getenv('PORT', 8000)), reload=True, access_log=True)