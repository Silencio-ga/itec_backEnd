from typing import Annotated

from fastapi import APIRouter, HTTPException, Path

from src.schemas.series_schemas import serie, serieUpdate

series_router = APIRouter()

# ========
# Datos
# ========

series: list[serie] = [
    {"id": 1, "nombre": "Breaking Bad", "genero": "Drama", "score": 54},
    {"id": 2, "nombre": "Stranger Things", "genero": "Ciencia ficción", "score": 75},
    {"id": 3, "nombre": "Game of Thrones", "genero": "Fantasía", "score": 12},
    {"id": 4, "nombre": "The Office", "genero": "Comedia", "score": 56},
    {"id": 5, "nombre": "Dark", "genero": "Misterio", "score": 93},
    {"id": 6, "nombre": "The Mandalorian", "genero": "Acción", "score": 67},
]

# ============
#    GET
# ============


# lista de series
@series_router.get("/", tags=["buscar series"], response_model=list[serie])
def obtener_series() -> list[serie]:
    return series


# buscar serie por ID
@series_router.get(
    "/{id}",
    tags=["buscar series"],
    response_model=serie,
    responses={
        404: {
            "description": "Serie no econtrado",
            "content": {
                "application/json": {"example": {"detail": "Serie no econtrado"}}
            },
        }
    },
)
def obtener_serie(id: Annotated[int, Path(gt=0)]) -> serie:
    for s in series:
        if s["id"] == id:
            return s
    raise HTTPException(status_code=404, detail="serie no encontrado")


# ============
#    POST
# ============


@series_router.post("/", tags=["añadir serie"], response_model=list[serie])
def agregar_serie(serie: serie) -> list[serie]:
    series.append(serie.model_dump())
    return series


# ============
#    PUT
# ============


@series_router.put(
    "/{id}",
    tags=["editar"],
    response_model=serieUpdate,
    responses={
        404: {
            "description": "Serie no econtrado",
            "content": {
                "application/json": {"example": {"detail": "Serie no econtrado"}}
            },
        }
    },
)
def editar_serie(id: Annotated[int, Path(gt=0)], serie: serieUpdate) -> serieUpdate:
    for s in series:
        if s["id"] == id:
            s["nombre"] = serie.nombre
            s["genero"] = serie.genero
            s["score"] = serie.score
            return serie
    raise HTTPException(status_code=404, detail="serie no encontrado")


# ============
#   DELETE
# ============


@series_router.delete(
    "/{id}",
    tags=["elimina"],
    response_model=list[serie],
    responses={
        404: {
            "description": "Serie no econtrado",
            "content": {
                "application/json": {"example": {"detail": "Serie no econtrado"}}
            },
        }
    },
)
def borrar_serie(id: Annotated[int, Path(gt=0)]) -> list[serie]:
    for s in series:
        if s["id"] == id:
            series.remove(s)
            return series
    raise HTTPException(status_code=404, detail="serie no encontrado")
