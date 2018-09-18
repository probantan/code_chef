import os

class Config():
    '''
    parent class config
    '''
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    pass

config_options = {
    'production':ProdConfig,
    'development':DevConfig,
    'test':TestConfig
}