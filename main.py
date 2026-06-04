from fastapi import FastAPI, Body, Path, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
app.title = "Nuestra primera APP"


#==========
#  Modelo
#==========

class serie(BaseModel):
    id: int
    nombre: str 
    genero: str
    score: int 

class serieUpdate(BaseModel):
    nombre: str 
    genero: str
    score: int 

#========
# Datos
#========

series = [
    {"id": 1,"nombre": "Breaking Bad","genero": "Drama", "score": 54},
    {"id": 2,"nombre": "Stranger Things","genero": "Ciencia ficción", "score": 75},
    {"id": 3,"nombre": "Game of Thrones","genero": "Fantasía", "score": 12},
    {"id": 4,"nombre": "The Office","genero": "Comedia", "score": 56},
    {"id": 5,"nombre": "Dark","genero": "Misterio", "score": 93},
    {"id": 6,"nombre": "The Mandalorian","genero": "Acción", "score": 67}
]

#============
#    GET 
#============

# lista de series
@app.get("/series", tags=["buscar series"])
def obtener_series() -> list[serie]:
    return series

# buscar serie por ID
@app.get("/series{id}", tags=["buscar series"])
def obtener_serie(id: Annotated[int, Path(gt=0)]) -> serie:
    for serie in series:
        if serie["id"] == id:
            return serie
    return []

#============
#    POST 
#============

@app.post("/agregar-serie", tags=["añadir serie"])
def agregar_serie(serie:serie) -> list[serie]:
    series.append(serie.model_dump())
    return series

#============
#    PUT 
#============

@app.put("/editar-juego/{id}", tags=["editar"])
def editar_serie(
    id: int,
    nombre: serieUpdate) -> serieUpdate: 
    for s in series:
        if s["id"] == id:
            s["nombre"] = serie.nombre
            s["genero"] = serie.genero
            s["score"] = serie.score
            return serie
    return {"mensaje": "serie no encontrado"}

#============
#   DELETE 
#============

@app.delete("/borrar-serie/{id}", tags=["elimina"])
def borrar_serie(id: int) -> list[serie]:
    for serie in series:
        if serie["id"] == id:
            series.remove(serie)
            return series
    return {"mensaje": "serie no encontrado"}

