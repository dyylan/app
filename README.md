## To do

1. Write a proper README.md

## How to run locally (email doesn't work locally)

1. Add some environment variables (.env file)

"""
FLASK_APP=main.py
FLASK_DEBUG=0
FLASK_CONFIG=development

# Secret keys
SECRET_KEY=*******
JWT_SECRET_KEY=*******

# General db stuff
DATABASE_URL=mysql+pymysql://*******:*******@mydb/main
DEV_DATABASE_URL=mysql+pymysql://*******:*******@mydb/main
MONGODB_URL=mongodb://*******:*******@mongodb/main
SQLALCHEMY_TRACK_MODIFICATIONS=False

# Email server
MAIL_USE_TLS=True
MAIL_SERVER=localhost
MAIL_PORT=25
MAIL_SUBJECT_PREFIX=[Sprig]
MAIL_SENDER==*******
MAIL_SENDER_NAME==*******

# Administrator user
ADMIN=*******
ADMIN_USERNAME==*******
ADMIN_PASSWORD==*******

# MySQL db
MYSQL_RANDOM_ROOT_PASSWORD=yes
MYSQL_DATABASE=main
MYSQL_USER==*******
MYSQL_PASSWORD==*******

# Mongo db 
MONGO_INITDB_DATABASE=main
MONGO_INITDB_ROOT_USERNAME==*******
MONGO_INITDB_ROOT_PASSWORD=*******
"""

1. Build the docker 

> $ docker-compose build

3. Spin up the dockers

> $ docker-compose up
