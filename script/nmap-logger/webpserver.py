from http.server import HTTPServer

httpd = HTTPServer(('127.0.0.1', 8000), pass)
httpd.serve_forever()
