# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el script Python y el archivo ratings.dat al contenedor
COPY app.py .
COPY ratings.dat .

# Instala las dependencias necesarias
RUN pip install flask pandas

# Expone el puerto 8080
EXPOSE 8080

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]