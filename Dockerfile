FROM python:3.8-slim-buster
LABEL maintainer="devcorujam@gmail.com"
ENV PYTHONUNBUFFERED=1

WORKDIR /backend

RUN apt-get update

# install requirements
RUN apt-get install git -y && apt-get install curl -y

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH = "${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false

# install dependencies
COPY poetry.lock pyproject.toml /backend/
RUN poetry install --no-root

# install project
COPY . /backend/
RUN poetry install