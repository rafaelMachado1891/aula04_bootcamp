FROM python:3.12.4-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para dentro do container
COPY . /app

# Criar e ativar o ambiente virtual
RUN python -m venv .venv

# Instalar dependências do projeto
RUN .venv/bin/pip install -r requirements.txt

# Definir o comando de entrada garantindo que o ambiente virtual está ativado
ENTRYPOINT ["/bin/sh", "-c", ". .venv/bin/activate && dbt run"]

