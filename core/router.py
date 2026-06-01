from core.parse import HttpRequest
class Router:
    def __init__(self):
        self.routes_table = {
            "GET" : {},
            "POST" : {}
        }
        
    def add_route(self, method, path, handler):
        method = method.upper()
        if method not in self.routes_table:
            self.routes_table[method] = {}
        self.routes_table[method][path] = handler

    def route(self, request_obj : HttpRequest):
        method = request_obj.method.upper()
        path = request_obj.path
        if method in self.routes_table:
            handler_func = self.routes_table[method][path]
            response = handler_func()
            return response
        return b"HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n404 Resource Not Found"
