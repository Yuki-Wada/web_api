import json

def login():
    data = json.loads(request.data.decode('utf-8'))
    conn = sqlite3.connect('api/static/aaa.sqlite3')
    result_table = pd.read_sql_query('SELECT * FROM registration reg where reg.name = "{}";'.format(data['user_name']), conn)
    result_table = result_table.query('password == "{}"'.format(data['password']))
    if len(result_table) > 0:
        expire = int((datetime.datetime.now() + datetime.timedelta(days=1)).timestamp())
        return jsonify({
            'token': True,
            'name': data['user_name'],
            'expire': expire
        })
    else:
        return jsonify({
            'token': False,
            'name': 'Guest',
            'expire': 0
        })

