# Etiqueta base: Utilizamos una imagen oficial de Python 3.9.13
FROM python:3.9.13-slim

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema operativo necesarias para mysqlclient
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libmariadb-dev-compat \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo requirements.txt primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos del microservicio al directorio de trabajo
COPY . .

# Exponer el puerto que utiliza tu aplicación (por ejemplo, el puerto 8000 para Django)
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]