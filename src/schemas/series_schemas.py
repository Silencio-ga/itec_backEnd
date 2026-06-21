from typing import Annotated
from pydantic import BaseModel, Field

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