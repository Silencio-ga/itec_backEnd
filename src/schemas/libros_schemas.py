from typing import Annotated
from pydantic import BaseModel, Field


class Libro(BaseModel):
    id: Annotated[int, Field(gt=0)]
    titulo: Annotated[
        str,
        Field(min_length=1, max_length=80, examples=["Cien años de soledad"]),
    ]
    autor: Annotated[
        str,
        Field(min_length=3, max_length=60, examples=["Gabriel García Márquez"]),
    ]
    paginas: Annotated[int, Field(gt=0, le=10000, examples=[496])]


class LibroUpdate(BaseModel):
    titulo: Annotated[
        str,
        Field(min_length=1, max_length=80, examples=["Cien años de soledad"]),
    ]
    autor: Annotated[
        str,
        Field(min_length=3, max_length=60, examples=["Gabriel García Márquez"]),
    ]
    paginas: Annotated[int, Field(gt=0, le=10000, examples=[496])]
