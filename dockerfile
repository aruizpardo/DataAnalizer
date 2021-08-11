FROM python:3.9

WORKDIR /app

# Instalar paquetes
RUN apt-get install bash

# Instalar paquetes de Python
RUN pip install -U Flask pandas

# Copiar ficheros
COPY ./flask/ .

# Ejecutar el flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]