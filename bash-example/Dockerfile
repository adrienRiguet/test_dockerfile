FROM python:3-alpine
LABEL org.opencontainers.image.source=https://github.com/adrienRiguet/test_dockerfile
WORKDIR /app

ARG default_name="name"
ENV NAME=${default_name}

# Copie le script dans le conteneur, dans le répertoire /app
COPY script.sh script-hello-world.sh
COPY script.py script.py
COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN PATH="/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exécute le script
CMD ["sh", "/app/script-hello-world.sh"]
