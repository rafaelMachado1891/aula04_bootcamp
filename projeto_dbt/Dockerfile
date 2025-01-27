FROM python:3.12-slim
RUN pip install poetry
WORKDIR /src
COPY . /src
RUN poetry install --no-root
RUN python -m pip install dbt-core dbt-postgres

# Configurar o profile no local padrão do DBT
RUN mkdir -p /root/.dbt
COPY profiles.yml /root/.dbt/profiles.yml

# Copiar o dbt_project.yml explicitamente
COPY northwind/dbt_project.yml /src/northwind/dbt_project.yml

# Definir o diretório de trabalho do projeto DBT
WORKDIR /src/northwind

CMD ["dbt", "run"]