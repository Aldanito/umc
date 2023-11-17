import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLASK_APP = 'app.py'
    FLASK_ENV = 'development'
    SECRET_KEY = 'anykey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_FILE_UPLOADER = 'upload'

    # configuration of mail
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'salomat423@gmail.com'
    MAIL_PASSWORD = '221502Ernur@'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    FLASK_ADMIN_SWATCH = 'flatly'  # lumen cyborg flatly

    # configuration of database
    SQLALCHEMY_DATABASE_URI = "postgresql://userimec:Pin.1234@172.16.1.13:5432/pyapp1"


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
