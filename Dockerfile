
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

ENV LISTEN_PORT=5000
EXPOSE 5000

ENV UWSGI_INI uwsgi.ini

ENV STATIC_URL /app/static

WORKDIR /app
ADD . /app

RUN python3 -m pip install pipenv
RUN pipenv install --system