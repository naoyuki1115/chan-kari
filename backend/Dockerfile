FROM python:3.11-slim-bullseye AS dev

WORKDIR /app/src

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt


# FROM python:3.11-slim-bullseye AS prod

# WORKDIR /app/src