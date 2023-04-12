FROM python:3.10-alpine

RUN pip install poetry


WORKDIR /workdir
COPY poetry.lock pyproject.toml /workdir/


RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi


COPY ./ ./
