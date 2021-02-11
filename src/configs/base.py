import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 's3cr3t'

    @staticmethod
    def init_app(app):
        pass
