from typing import Annotated

from fastapi import APIRouter, HTTPException, Path

from src.schemas.libros_schemas import Libro, LibroUpdate

libros_router = APIRouter()

libros: list[Libro] = [
    {
        "id": 1,
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "paginas": 496,
    },
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "paginas": 328},
    {
        "id": 3,
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "paginas": 96,
    },
    {
        "id": 4,
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "paginas": 863,
    },
    {
        "id": 5,
        "titulo": "La sombra del viento",
        "autor": "Carlos Ruiz Zafón",
        "paginas": 576,
    },
    {
        "id": 6,
        "titulo": "Fuego y sangre",
        "autor": "George R.R. Martin",
        "paginas": 856,
    },
]


@libros_router.get("/", tags=["buscar libros"], response_model=list[Libro])
def obtener_libros() -> list[Libro]:
    return libros


@libros_router.get(
    "/{id}",
    tags=["buscar libros"],
    response_model=Libro,
    responses={
        404: {
            "description": "Libro no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Libro no encontrado"}}
            },
        }
    },
)
def obtener_libro(id: Annotated[int, Path(gt=0)]) -> Libro:
    for s in libros:
        if s["id"] == id:
            return s
    raise HTTPException(status_code=404, detail="libro no encontrado")


@libros_router.post("/", tags=["añadir libro"], response_model=list[Libro])
def agregar_libro(libro: Libro) -> list[Libro]:
    libros.append(libro.model_dump())
    return libros


@libros_router.put(
    "/{id}",
    tags=["editar"],
    response_model=LibroUpdate,
    responses={
        404: {
            "description": "Libro no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Libro no encontrado"}}
            },
        }
    },
)
def editar_libro(id: Annotated[int, Path(gt=0)], libro: LibroUpdate) -> LibroUpdate:
    for l in libros:
        if l["id"] == id:
            l["titulo"] = libro.titulo
            l["autor"] = libro.autor
            l["paginas"] = libro.paginas
            return libro
    raise HTTPException(status_code=404, detail="libro no encontrado")


@libros_router.delete(
    "/{id}",
    tags=["elimina"],
    response_model=list[Libro],
    responses={
        404: {
            "description": "Libro no encontrado",
            "content": {
                "application/json": {"example": {"detail": "Libro no encontrado"}}
            },
        }
    },
)
def borrar_libro(id: Annotated[int, Path(gt=0)]) -> list[Libro]:
    for s in libros:
        if s["id"] == id:
            libros.remove(s)
            return libros
    raise HTTPException(status_code=404, detail="libro no encontrado")
