def handle_home():
    return b"HTTP/1.1 200 OK\r\n\r\nWelcome to Home Page"

def handle_profile():
    return b"HTTP/1.1 200 OK\r\n\r\nThis is your Profile"

def handle_login():
    return b"HTTP/1.1 200 OK\r\n\r\nStarting Login..."
