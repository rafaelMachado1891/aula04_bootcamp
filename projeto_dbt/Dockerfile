FROM python:3.12-slim
RUN pip install poetry
WORKDIR /src
COPY . /src
RUN poetry install --no-root
WORKDIR /src/northwind
CMD ["dbt-postgres", "run"]