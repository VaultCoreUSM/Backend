# Usa una imagen base de Python más compatible
FROM python:3.13-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala herramientas del sistema necesarias
RUN apt-get update && apt-get install -y \
    ffmpeg \
    wkhtmltopdf \
    build-essential \
    curl \
    libxrender1 \
    libxtst6 \
    libjpeg-dev \
    libfontconfig1 \
    libx11-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requerimientos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación
COPY ./app /app/app

# Expone el puerto 8000 para Uvicorn
EXPOSE 8000

# Comando por defecto para ejecutar Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

