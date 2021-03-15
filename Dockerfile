FROM python:3.8-slim-buster
LABEL maintainer="devcorujam@gmail.com"

WORKDIR /backend

# install poetry
RUN apt-get update && apt-get install curl -y
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH = "${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false