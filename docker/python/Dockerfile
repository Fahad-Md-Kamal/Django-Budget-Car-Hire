FROM python:3.8

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./docker/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
