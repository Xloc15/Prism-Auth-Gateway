import time
def handle_home():
    time.sleep(3) #Mô phỏng thời gian Server xử lý 1 Client request
    return b"HTTP/1.1 200 OK\r\n\r\nWelcome to Home Page"

def handle_profile():
    time.sleep(3) #Mô phỏng thời gian Server xử lý 1 Client request
    return b"HTTP/1.1 200 OK\r\n\r\nThis is your Profile"

def handle_login():
    time.sleep(3) #Mô phỏng thời gian Server xử lý 1 Client request
    return b"HTTP/1.1 200 OK\r\n\r\nStarting Login..."
