from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()
app.title = "Nuestra primera APP"


#==========
#  Modelo
#==========

class serie(BaseModel):
    id: Annotated[int, Field(gt=0)]
    nombre: Annotated[
        str,
        Field(min_length=3, max_length=35, examples= ["Breaking Bad"], default= "Stranger Things"),
        ]
    genero: Annotated[
        str,
        Field(min_length=3, max_length=35, examples= ["Drama"], default= "Ciencia ficción")
    ]
    score: Annotated[int, Field(gt=0, le=100, examples=[50], default=50)]

class serieUpdate(BaseModel):
    nombre: Annotated[
        str,
        Field(min_length=3, max_length=35, examples= ["Breaking Bad"], default= "Stranger Things"),
        ]
    genero: Annotated[
        str,
        Field(min_length=3, max_length=35, examples= ["Drama"], default= "Ciencia ficción")
    ]
    score: Annotated[int, Field(gt=0, le=100, examples=[50], default=50)]

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
@app.get("/series", tags=["buscar series"], response_model=list[serie])
def obtener_series() -> list[serie]:
    return series

# buscar serie por ID
@app.get("/series/{id}", 
    tags=["buscar series"], 
    response_model=serie,
    responses={
        404: {
        "description": "Serie no econtrado", 
        "content": {
            "application/json": {"example": {"detail": "Serie no econtrado"}}
            }
        }
    },
)
def obtener_serie(id: Annotated[int, Path(gt=0)]) -> serie:
    for serie in series:
        if serie["id"] == id:
            return serie
    raise HTTPException(status_code=404, detail="serie no encontrado")

#============
#    POST 
#============

@app.post("/agregar-serie", tags=["añadir serie"], response_model=list[serie])
def agregar_serie(serie:serie) -> list[serie]:
    series.append(serie.model_dump())
    return series

#============
#    PUT 
#============

@app.put(
    "/editar-serie/{id}", 
    tags=["editar"],
    response_model=serieUpdate,
    responses={
        404: {
        "description": "Serie no econtrado", 
        "content": {
            "application/json": {"example": {"detail": "Serie no econtrado"}}
            }
        }
    },)
def editar_serie(
    id: int,
    serie: serieUpdate) -> serieUpdate: 
    for s in series:
        if s["id"] == id:
            s["nombre"] = serie.nombre
            s["genero"] = serie.genero
            s["score"] = serie.score
            return serie
    raise HTTPException(status_code=404, detail="serie no encontrado")

#============
#   DELETE 
#============

@app.delete("/borrar-serie/{id}", 
    tags=["elimina"], 
    response_model=list[serie],
    responses={
        404: {
        "description": "Serie no econtrado", 
        "content": {
            "application/json": {"example": {"detail": "Serie no econtrado"}}
            }
        }
    },
)
def borrar_serie(id: int) -> list[serie]:
    for serie in series:
        if serie["id"] == id:
            series.remove(serie)
            return series
    raise HTTPException(status_code=404, detail="serie no encontrado")

