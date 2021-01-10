from api.views import app, sockets
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from flask_sockets import worker

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8895
    host_port = (host, port)

    server = WSGIServer(
        host_port,
        app,
        handler_class=WebSocketHandler
    )
    server.serve_forever()
