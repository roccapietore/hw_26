import base64
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "you-will-never-guess")
    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        os.path.dirname(BASEDIR), "project.db"
    )


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'.format(
        db_user=os.getenv('POSTGRES_USER'),
        db_pass=os.getenv('POSTGRES_PASSWORD'),
        db_host=os.getenv('POSTGRES_HOST', 'localhost'),
        db_port=os.getenv('POSTGRES_PORT', 5432),
        db_name=os.getenv('POSTGRES_DB'),
    )



def choose_config():
    if 'production' == os.getenv('FLASK_ENV'):
        return ProductionConfig
    return DevelopmentConfig
