import os


class Config:
    '''
    General configuration parent class
    '''

    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://karimi:karimi@localhost/blog'

    SECRET_KEY = os.environ.get('SECRET_KEY')


    WTF_CSRF_ENABLED = True

    #SQLALCHEMY_TRACK_MODIFICATIONS=False

   # ADMIN_PASSWORD='31989796'

   # ADMIN_USERNAME='karimikim'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
    
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}