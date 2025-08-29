# syntax=docker/dockerfile:1
FROM python:3.12-slim

# Evitar buffering y archivos .pyc
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Instalar dependencias del sistema necesarias para drivers y compilación
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero para aprovechar cache de docker
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# Crear usuario no root
RUN useradd --create-home appuser
USER appuser

# Copiar el resto del código
COPY --chown=appuser:appuser . .

# Puerto expuesto por FastAPI (uvicorn)
EXPOSE 8000

# Comando por defecto (producción simple con uvicorn).
# Si prefieres usar gunicorn + uvicorn workers, sustitúyelo por la línea adecuada.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
