#from urllib import response
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
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/message")
async def rec_msg(message: dict):
    print(str(message))
    input_data_to_db(message)
    return

@app.get("/latest")
async def latest():
    return data_list_latest()

@app.get("/data/{id}")
async def get_data(id: int):
    return data_list_by_id(id)

@app.get("/data/all")
async def get_all():
    return data_list_all()