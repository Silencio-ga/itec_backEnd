from fastapi import FastAPI, Body

app = FastAPI()
app.title = ""

series = [
    {"id": 1,"nombre": "Breaking Bad","genero": "Drama"},
    {"id": 2,"nombre": "Stranger Things","genero": "Ciencia ficción"},
    {"id": 3,"nombre": "Game of Thrones","genero": "Fantasía"},
    {"id": 4,"nombre": "The Office","genero": "Comedia"},
    {"id": 5,"nombre": "Dark","genero": "Misterio"},
    {"id": 6,"nombre": "The Mandalorian","genero": "Acción"}
]

@app.get("/series", tags=["buscar series"])
def obtener_series():
    return series

@app.get("/series{id}", tags=["buscar series"])
def obtener_serie(id: int):
    for serie in series:
        if serie["id"] == id:
            return serie
    return []

@app.post("/agregar-serie", tags=["añadir serie"])
def agregar_serie(id: int = Body(), nombre: str = Body(), genero: str = Body()):
    series.append({"id": id, "nombre": nombre, "genero": genero})
    return series

@app.put("/editar-juego/{id}", tags=["editar"])
def editar_serie(id: int, nombre: str = Body(), genero: str = Body()): 
    for serie in series:
        if serie["id"] == id:
            serie["nombre"] = nombre
            serie["genero"] = genero
            return serie
    return {"mensaje": "serie no encontrado"}

@app.delete("/borrar-serie/{id}", tags=["elimina"])
def borrar_serie(id: int):
    for serie in series:
        if serie["id"] == id:
            series.remove(serie)
            return series
    return {"mensaje": "serie no encontrado"}
