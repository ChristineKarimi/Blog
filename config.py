class Config:
  
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://karimi:karimi@localhost/blog'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}
 
