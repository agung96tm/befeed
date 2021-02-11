from flask import Flask

# env
from configs.dev import DevelopmentConfig
from configs.prod import ProductionConfig
from configs.test import TestConfig

# blueprints
from core.http import http as http_blueprint
from apps.feed import feed as feed_blueprint


configs = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,

    #
    'default': DevelopmentConfig,
}


def register_blueprints(app: Flask):
    app.register_blueprint(feed_blueprint)
    app.register_blueprint(http_blueprint)


def initialize_configs(app: Flask, config_env):
    app.config.from_object(configs[config_env])
    register_blueprints(app)
