# https://medium.com/c0d1um/building-django-docker-image-with-alpine-32de65d2706
FROM python:3.10.4

# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
# Python env vars
ENV PYTHONUNBUFFERED=1 \
    # https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
    PYTHONDONTWRITEBYTECODE=1 \
    # Pip env vars (https://pip.pypa.io/en/stable/user_guide/#environment-variables)
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry env vars (https://python-poetry.org/docs/configuration/#using-environment-variables)
    POETRY_VERSION=1.1.13 \
    POETRY_NO_INTERACTION=1

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

RUN poetry config virtualenvs.create false

RUN mkdir /app
WORKDIR /app

COPY backend/poetry.lock backend/pyproject.toml /app/

RUN poetry install --no-dev
COPY . /app/

ENV PYTHONPATH=/app/src:$PYTHONPATH

EXPOSE 8081
