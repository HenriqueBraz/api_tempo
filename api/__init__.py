from flask import Flask


app = Flask(__name__)

from api.services.api_tempo import apiTempo

DEBUG = True





