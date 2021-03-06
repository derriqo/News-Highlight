import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_URL  ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    SOURCE_API_KEY = os.environ.get('SOURCE_API_KEY')
    ARTICLES_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}