# Usar como base la imagen de Node.js 12.18.1
FROM node:12.18.1-slim

# Configurar directorio de trabajo
WORKDIR /opt/microservices/

# Copiar archivos necesarios al contenedor
COPY package.json .
COPY ratings.js .

# Instalar las dependencias
RUN npm install

# Configurar variables de entorno
ENV SERVICE_VERSION=v1
ENV ENABLE_RATINGS=true

# Exponer el puerto 9080
EXPOSE 9080

# Ejecutar el servicio
CMD ["node", "ratings.js", "9080"]
