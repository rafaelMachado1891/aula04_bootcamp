FROM python:3.12.4-slim

# Definir variáveis de ambiente para Poetry e DBT
ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_PATH="/app/.venv" \
    DBT_PROFILES_DIR="/app/projeto_dbt"

# Instalar o Poetry
RUN pip install poetry

# Criar diretório do projeto e definir permissões
WORKDIR /app

# Copiar apenas o arquivo de dependências para otimizar cache
COPY pyproject.toml poetry.lock ./

# Criar o ambiente virtual antes de copiar todo o código
RUN poetry install --no-root

# Agora copiar o restante do código
COPY . /app

# Definir o comando de execução
ENTRYPOINT ["poetry", "run", "dbt", "run"]