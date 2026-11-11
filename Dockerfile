
# Imagen base de Python
FROM python:3.12-slim

# Directorio de trabajo del contenedor
WORKDIR /app

# Instalacion de dependencias
RUN pip install --no-cache-dir fastapi uvicorn

# Copiar la aplicacion al contenedor
COPY app.py .

# Puerto utilizado por la aplicacion
EXPOSE 8000

# Comando para iniciar FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

