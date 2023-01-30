# for develop
FROM python:3.11-bullseye AS dev

WORKDIR /app/src

COPY requirements.txt ./

RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql \
    vim

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r requirements.txt

# for production
FROM python:3.11-slim-bullseye AS prod

WORKDIR /app

COPY --from=dev /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=dev /usr/local/bin/uvicorn /usr/local/bin/uvicorn 

RUN apt-get update && apt-get install -y \
    libpq-dev && \
    apt-get clean

COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]