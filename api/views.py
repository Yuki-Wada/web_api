import json
import datetime
import time
import pandas as pd
import sqlite3

import gevent
from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from flask_cors import CORS
from flask_sockets import Sockets

from api.models.train_maze import ValueIterTrainer, SarsaLambdaTrainer

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'hoge'
CORS(app)
sockets = Sockets(app)

trainer = None

@app.route('/', methods=['GET'])
def root():
    return 'test'

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = json.loads(request.data.decode('utf-8'))
    conn = sqlite3.connect('api/static/aaa.sqlite3')

    sql_command = f"""
    SELECT
        *
    FROM REGISTRATIOJ
    WHERE
        NAME = '{data['user_name']}' AND
        PASSWORD = 'data['password']'
    """
    result_table = pd.read_sql_query(sql=sql_command, con=conn)
    if len(result_table) > 0:
        expire = int((datetime.datetime.now() + datetime.timedelta(days=1)).timestamp())
        json_data = {
            'token': True,
            'name': data['user_name'],
            'expire': expire
        }
        return jsonify(json_data)

    else:
        json_data = {
            'token': False,
            'name': 'Guest',
            'expire': 0
        }

    return jsonify(json_data)

def create_trainer(data):
    if data['algorithm'] == 'valueiter':
        return ValueIterTrainer(
            iter_count=2000,
        )
    elif data['algorithm'] == 'sarsalambda':
        return SarsaLambdaTrainer(
            alpha=0.1,
            gamma=0.95,
            epsilon=0.1,
            lambda_value=0.2,
            iter_count=2000,
        )

@sockets.route('/train_maze')
def train_maze(ws):
    ws.send(json.dumps({'status': 'start_connection'}))
    while not ws.closed:
        gevent.sleep(0.1)
        message = ws.receive()
        if message:
            recieved = json.loads(message)
            if recieved['status'] == 'initialize_trainer':
                trainer = create_trainer(recieved['config'])
                ws.send(json.dumps({'status': 'trainer_construction'}))
            elif recieved['status'] == 'trainer_run':
                result = trainer.run()
                ws.send(json.dumps({
                    'status': 'step_maze',
                    'maze_color': result,
                }))
