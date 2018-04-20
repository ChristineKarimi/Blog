import os


class Config:
    '''
    General configuration parent class
    '''

    


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

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://karimi:karimi@localhost/blog'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
