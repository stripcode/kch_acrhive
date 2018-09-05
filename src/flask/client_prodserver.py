from gevent.wsgi import WSGIServer
from app import createClientApp

http_server = WSGIServer(('', 8081), createClientApp())
http_server.serve_forever()