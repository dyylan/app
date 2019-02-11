import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    ADMIN = os.environ.get('ADMIN')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or os.environ.get('SECRET_KEY') 
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = os.environ.get('MAIL_SUBJECT_PREFIX')
    MAIL_SENDER = os.environ.get('MAIL_SENDER')
    MAIL_SENDER_NAME = os.environ.get('MAIL_SENDER_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') \
        or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    MONGO_URI = os.environ.get('MONGODB_URL') + '?authSource=admin'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    MONGO_URI = os.environ.get('MONGODB_URL') + '?authSource=admin'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    MONGO_URI = os.environ.get('MONGODB_URL') + '?authSource=admin'


config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }
