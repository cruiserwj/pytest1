from wsgiref.simple_server import make_server
from hello import application
httpd = make_server('127.0.0.1',8000,application)
print 'start'
httpd.serve_forever()