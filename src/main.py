from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.series_router import series_router

app = FastAPI()
app.title = "Gabriel acuña - tp evaluativo FastAPI"

origenes_permitidos = [
    "http://localhost:3000",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origenes_permitidos,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=series_router, prefix="/series")
