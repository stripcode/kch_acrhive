from gevent.wsgi import WSGIServer
from app import createAdminApp

http_server = WSGIServer(('', 8082), createAdminApp())
http_server.serve_forever()