# Usa una imagen base de Python optimizada para producción
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo los archivos necesarios para instalar dependencias primero (optimiza la caché de Docker)
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que corre la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación (ajusta según el framework usado)
CMD ["python", "/app/currency_converter.py"]

