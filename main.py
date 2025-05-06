#from urllib import response
from datetime import datetime, timedelta
from typing import Annotated
from fastapi import FastAPI, Response, status, Header
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from admin_db import *

#rights = ["all", "user", None]


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:*",
    "*"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


last_msg_time = datetime.now() - timedelta(seconds=10)


@app.post("/message")
async def rec_msg(message: dict):
    message = str(message)
    input_data_to_db(message)
    global last_msg_time
    last_msg_time = datetime.now()
    print(str(message), " ", last_msg_time)
    return Response(content=None, status_code=200)

@app.get("/latest")
async def latest():
    return data_list_latest()

@app.get("/data/{id}")
async def get_data(id: int):
    return data_list_by_id(id)

@app.get("/all")
async def get_all():
    return data_list_all()

@app.get("/online")
async def online():
    if (datetime.now() - timedelta(seconds=10)) < last_msg_time:
        return True
    else: return False