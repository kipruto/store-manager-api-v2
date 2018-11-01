import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    # Development database connection url
    url = "dbname='api' host='127.0.0.1' port='5432' user='admin' password='admin123'"
    os.environ['ENV'] = 'development'


class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True
    # test database URl ..
    # url = "dbname='api_tests' host='127.0.0.1' port='5432' user='admin' password='admin123'"
    # os.environ['ENV'] = 'testing'


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
