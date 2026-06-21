from fastapi import FastAPI
from src.routers.series_router import series_router

app = FastAPI()
app.title = "Nuestra primera APP"

app.include_router(router=series_router, prefix="/series")


