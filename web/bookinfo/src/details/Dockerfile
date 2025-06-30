# Usar la imagen base de Ruby 2.7.1 slim
FROM ruby:2.7.1-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /opt/microservices

# Copiar el archivo details.rb al directorio de trabajo
COPY details.rb /opt/microservices/

# Establecer las variables de entorno necesarias
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

# Exponer el puerto 9080
EXPOSE 9080

# Comando para ejecutar el servicio
CMD ["ruby", "details.rb", "9080"]
