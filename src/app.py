from flask import Flask

from configs import initialize_configs


def create_app(config_env):
    app = Flask(__name__)
    initialize_configs(app, config_env)

    return app
