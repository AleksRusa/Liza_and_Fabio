import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

app.include_router(routers.router)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
