from flask import Flask, jsonify, url_for
from werkzeug.utils import redirect

from api.services. api_tempo import apiTempo

app = Flask(__name__)

@app.route("/favicon.ico")
def favicon():
    return redirect(url_for('index', flag=1))

@app.route('/', methods=["GET"])
def index():
    return 'Digite /returnstuff/elemento/seletor_css/page'

@app.route('/returnstuff/<string:elemento>/<string:seletor_css>/<path:page>', methods=["GET"])
def returnstuff(elemento, seletor_css, page):
    api = apiTempo()
    return jsonify(api.search_element(elemento, seletor_css, page))

if __name__ == '__main__':
    app.run(debug=True)