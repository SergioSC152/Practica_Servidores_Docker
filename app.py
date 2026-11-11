
import os
from fastapi import FastAPI

app = FastAPI(
    title="Taller de Servidores Docker",
    description="API para comprobar el balanceo de carga",
    version="1.0.0"
)

SERVIDOR = os.getenv("SERVIDOR", "Servidor desconocido")


@app.get("/")
def inicio():
    return {
        "mensaje": "El servidor esta funcionando correctamente",
        "servidor": SERVIDOR
    }

@app.get("/salud")
def salud():
    return {
        "estado": "activo",
        "servidor": SERVIDOR
    }

