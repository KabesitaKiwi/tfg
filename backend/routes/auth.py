from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from config.db import get_connection

# Creamos un router para manejar autenticación
router = APIRouter()

# Modelo para recibir los datos del login
class LoginRequest(BaseModel):
    email: str
    contraseña: str

@router.post("/login")
def login(request: LoginRequest):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Error al conectar con la base de datos")

    cursor = conn.cursor(dictionary=True)
    
    # Consultamos si el usuario existe
    query = "SELECT nombre FROM usuarios WHERE email = %s AND contrasenya = %s"
    cursor.execute(query, (request.email, request.contraseña))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        return {"nombre": user["nombre"]}
    else:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
