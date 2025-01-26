FROM projeto_dbt/python:3.12-slim
RUN pip install poetry
WORKDIR /src
COPY . /src
RUN poetry install --no-dev
WORKDIR /src/northwind
CMD ["dbt", "run"]