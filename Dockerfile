# Use the official Python slim image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt requirements.txt
    
# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo da aplicação para o diretório de trabalho
COPY . .

ENV PYTHONPATH=/app