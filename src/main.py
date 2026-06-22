from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.libros_router import libros_router

app = FastAPI()
app.title = "Gabriel acuña - tp evaluativo FastAPI"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=libros_router, prefix="/libros")
