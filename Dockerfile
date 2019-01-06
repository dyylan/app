
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

# By default, allow unlimited file sizes, modify it to limit the file sizes
# To have a maximum of 1 MB (Nginx's default) change the line to:
# ENV NGINX_MAX_UPLOAD 1m
#ENV NGINX_MAX_UPLOAD 0

#ENV LISTEN_PORT 80

#ENV UWSGI_INI uwsgi.ini
#ENV STATIC_URL /static
#ENV STATIC_PATH /app/static
#ENV STATIC_INDEX 0

#RUN python3 -m pip install pipenv
#RUN pipenv install --system
 
COPY ./app/requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app
#WORKDIR /app

#ENV PYTHONPATH=/app

# Copy start.sh script that will check for a /app/prestart.sh script and run it before starting the app
#COPY start.sh /start.sh
#RUN chmod +x /start.sh

# Copy the entrypoint that will generate Nginx additional configs
#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

#ENTRYPOINT ["/entrypoint.sh"]

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Supervisor, which in turn will start Nginx and uWSGI
#CMD ["/start.sh"]

