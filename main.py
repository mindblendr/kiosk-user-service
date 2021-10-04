from dotenv import load_dotenv
load_dotenv()
import os
import uvicorn
from fastapi import FastAPI
from bin.router import initiate_routers
from bin.main_db import init_main_db

if os.getenv('ENVIRONMENT', 'dev') == 'prod':
    app = FastAPI(debug=False, docs_url=None)
else:
    app = FastAPI(debug=True)

initiate_routers(app)
init_main_db(app)

if __name__ == '__main__':
    uvicorn.run("main:app", port=int(os.getenv('PORT', 8000)), reload=True, access_log=True)