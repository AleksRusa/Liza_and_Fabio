import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from routers import router
import uvicorn

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://127.0.0.1:8000",
#         "http://localhost:8000",
#     ],
# )

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        reload=True,
        port=8000,
    )
