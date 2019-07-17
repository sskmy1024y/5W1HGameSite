# coding: utf-8

from flask import Flask, request, make_response, redirect, abort
from when import When
import json

When.initDatabase()

app = Flask(__name__)

@app.route('/api/when', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        params = request.get_json()
        result = When.register(params['word'])
        if result:
            return json.dumps(result.toJSON()), 201
        else:
            return json.dumps('409 Conflict'), 409
    elif request.method == 'GET':
        return When.getRandom(), 200


