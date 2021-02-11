from flask import Blueprint

http = Blueprint('http', __name__)

from . import views
