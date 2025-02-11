FROM python:3.12.4-slim

# Instalar o Poetry
RUN pip install poetry

# Copiar todo o restante do código
COPY . /app

# Definir o diretório de trabalho na raiz do projeto
WORKDIR /app

# Instalar as dependências antes de copiar tudo (melhor cache)
RUN poetry install --no-root


# Comando para rodar o dbt
ENTRYPOINT ["poetry", "run", "dbt", "run"]