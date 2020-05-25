from api import app
from flask import jsonify, url_for
from werkzeug.utils import redirect
from api.services.api_tempo import apiTempo


@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return redirect(url_for('index'))


@app.route('/', methods=["GET"])
def index():
    return 'Digite:  https://returnstuff-tempo.herokuapp.com/returnstuff/elemento/seletor_css/page'


@app.route('/returnstuff/<string:elemento>/<string:seletor_css>/<path:page>', methods=["GET"])
def returnstuff(elemento, seletor_css, page):
    api = apiTempo()
    return jsonify(api.search_element(elemento, seletor_css, page))
