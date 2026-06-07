from core.parse import HttpRequest
PUBLIC_PATH = ["/", "/home","/login"]

class AuthGuard:
    def extract_token(self, request_obj : HttpRequest):
        if not request_obj.headers:
            return None
        if 'authorization' not in request_obj.headers:
            return None
        author_line = request_obj.headers['authorization']
        if author_line.startswith("bearer "):
            token = author_line[7:]
            if not token:
                return None
            return token
        return None
    
    def is_authorized(self, request_obj : HttpRequest): 
        if request_obj.path in PUBLIC_PATH:
            return True
        token = self.extract_token(request_obj)
        if token == "prism_secret_token_123":
            return True
        return False
