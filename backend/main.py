from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db import get_connection  # Importamos la función correctamente

app = FastAPI()

# Configurar CORS para permitir peticiones del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "¡API funcionando con FastAPI!"}

@app.get("/usuarios")
@app.get("/usuarios")
def obtener_usuarios():
    conn = get_connection()
    if not conn:
        return {"error": "No se pudo conectar a la base de datos"}
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")  # Asegúrate de que la tabla existe
    usuarios = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return {"usuarios": usuarios}  # Devolver en formato JSON


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
