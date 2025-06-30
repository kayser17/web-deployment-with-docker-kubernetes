# Usar Python 3.7.7 como base para la imagen
FROM python:3.7.7-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app

# Instalar las dependencias especificadas en requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Configurar una variable de entorno para el grupo
ENV GROUP_NUM=29

# Exponer el puerto 9080 para que sea accesible
EXPOSE 9080

# Comando para ejecutar la aplicación en el puerto 9080 (5080 Docker y productpage_monolith.py)
CMD ["python3", "productpage.py", "9080"]
