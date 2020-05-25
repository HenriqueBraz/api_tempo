from flask import Flask


app = Flask(__name__)

from api.services import api_tempo
from api.views import api_view

DEBUG = True





