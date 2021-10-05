from dotenv import load_dotenv
load_dotenv()
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bin.router import initiate_routers
from bin.main_db import init_main_db

if os.getenv('ENVIRONMENT', 'dev') == 'prod':
    app = FastAPI(debug=False, docs_url=None)
else:
    app = FastAPI(debug=True)

# add cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

initiate_routers(app)
init_main_db(app)

if __name__ == '__main__':
    uvicorn.run("main:app", port=int(os.getenv('PORT', 8000)), reload=True, access_log=True)