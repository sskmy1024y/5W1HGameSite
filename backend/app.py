# coding: utf-8

from flask import Flask, request, make_response, redirect, abort
from element import Element, When, Where, Why, What, Who, How
import json

Element.initAllDatabase()

app = Flask(__name__)


@app.route('/api/all', methods=['GET', 'POST'])
def registerAll():
    if request.method == 'POST':
        params = request.get_json()
        result = []

        if params['when']:
            result['when'] = When.register(params['when']).toJSON()
        if params['where']:
            result['where'] = Where.register(params['where']).toJSON()
        if params['who']:
            result['who'] = Who.register(params['who']).toJSON()
        if params['what']:
            result['what'] = What.register(params['what']).toJSON()
        if params['why']:
            result['why'] = Why.register(params['why']).toJSON()
        if params['how']:
            result['how'] = How.register(params['how']).toJSON()

        if result:
            return json.dumps(result), 201
        else:
            return json.dumps('409 Conflict'), 409
    elif request.method == 'GET':
        result = {}
        result['when'] = When.getRandom()
        result['where'] = Where.getRandom()
        result['who'] = Who.getRandom()
        result['what'] = What.getRandom()
        result['why'] = Why.getRandom()
        result['how'] = How.getRandom()

        if result:
            return json.dumps(result), 200
        else:
            return "", 204


@app.route('/api/when', methods=['GET', 'POST'])
def registerWhen():
    if request.method == 'POST':
        params = request.get_json()
        result = When.register(params['word'])
        if result:
            return json.dumps(result.toJSON()), 201
        else:
            return json.dumps('409 Conflict'), 409
    elif request.method == 'GET':
        word = When.getRandom()
        if word:
            return word, 200
        else:
            return "", 204


@app.route('/api/where', methods=['GET', 'POST'])
def registerWhere():
    if request.method == 'POST':
        params = request.get_json()
        result = Where.register(params['word'])
        if result:
            return json.dumps(result.toJSON()), 201
        else:
            return json.dumps('409 Conflict'), 409
    elif request.method == 'GET':
        word = Where.getRandom()
        if word:
            return word, 200
        else:
            return "", 204


@app.route('/api/who', methods=['GET', 'POST'])
def registerWho():
    if request.method == 'POST':
        params = request.get_json()
        result = Who.register(params['word'])
        if result:
            return json.dumps(result.toJSON()), 201
        else:
            return json.dumps('409 Conflict'), 409
    elif request.method == 'GET':
        word = Who.getRandom()
        if word:
            return word, 200
        else:
            return "", 204


@app.route('/api/why', methods=['GET', 'POST'])
def registerWhy():
    if request.method == 'POST':
        params = request.get_json()
        result = Why.register(params['word'])
        if result:
            return json.dumps(result.toJSON()), 201
        else:
            return json.dumps('409 Conflict'), 409
    elif request.method == 'GET':
        word = Why.getRandom()
        if word:
            return word, 200
        else:
            return "", 204


@app.route('/api/what', methods=['GET', 'POST'])
def registerWhat():
    if request.method == 'POST':
        params = request.get_json()
        result = What.register(params['word'])
        if result:
            return json.dumps(result.toJSON()), 201
        else:
            return json.dumps('409 Conflict'), 409
    elif request.method == 'GET':
        word = What.getRandom()
        if word:
            return word, 200
        else:
            return "", 204


@app.route('/api/how', methods=['GET', 'POST'])
def registerHow():
    if request.method == 'POST':
        params = request.get_json()
        result = How.register(params['word'])
        if result:
            return json.dumps(result.toJSON()), 201
        else:
            return json.dumps('409 Conflict'), 409
    elif request.method == 'GET':
        word = How.getRandom()
        if word:
            return word, 200
        else:
            return "", 204
