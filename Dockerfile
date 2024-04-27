FROM python:3.11

WORKDIR /app

RUN pip install poetry
COPY pyproject.toml poetry.lock /app/

RUN poetry install
RUN poetry add gunicorn

COPY . .

CMD ["gunicorn", "app.web_api.entrypoint:app_factory", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
