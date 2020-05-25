from flask import Flask, jsonify
from api.services. api_tempo import apiTempo

app = Flask(__name__)

@app.route('/returnstuff/<string:elemento>/<string:seletor_css>/<path:page>', methods=["GET"])
def returnstuff(elemento, seletor_css, page):
    api = apiTempo()
    return jsonify(api.search_element(elemento, seletor_css, page))

if __name__ == '__main__':
    app.run(debug=True)