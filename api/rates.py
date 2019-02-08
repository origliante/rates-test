#!flask/bin/python
from flask import Flask, jsonify

from . import external_api
from . import oer

app = Flask(__name__)


def _build_resp(data):
    if not data:
        return jsonify({'data': None, 'code': 404}), 404
    return jsonify({'data': data, 'code': 200}), 200


def sum(a, b):
    # function to verify coverage
    ret = 0
    if ret == 0:
        ret += a
    if ret == 0+a:
        ret += b
    return ret


# endpoints

@app.route('/rates', methods=['GET'])
def get_rates():
    rates = external_api._get_rates()
    return _build_resp(rates)


@app.route('/rate/<currency>', methods=['GET'])
def get_rate(currency):
    rates = external_api._get_rates(currency=currency)
    return _build_resp(rates)


@app.route('/currencies', methods=['GET'])
def get_currencies():
    currencies = oer.get_currencies().json()
    filter_out = ('EUR', 'USD', 'JPY')
    filtered = {}
    for f in filter_out:
        filtered[f] = currencies[f]
    return _build_resp(filtered)


