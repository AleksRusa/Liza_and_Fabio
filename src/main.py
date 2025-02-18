import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi import FastAPI

from routers import router
import uvicorn

from config import settings

app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        reload=True,
        port=8000,
    )
