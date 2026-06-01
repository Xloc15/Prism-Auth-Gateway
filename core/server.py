import socket 
import time
from core.parse import HttpRequest
from core.router import Router
from core.service import *

HOST = '127.0.0.1'
PORT = 8080

router = Router()
router.add_route("GET", "/",handle_home)
router.add_route("GET","/profile", handle_profile)
router.add_route("GET", "/login", handle_login)
print("ROUTER TABLE: ")
print(router.routes_table)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print(f"Server lắng nghe tại IP: {HOST}, PORT: {PORT}")
    s.listen()
    print("Server đang bắt đầu lắng nghe")
    try:
        while True:     
            connect, addr = s.accept()
            print(f"Server đã kết nối với Client: {addr}")
            with connect as conn:
                # Phân tích Header request Client gửi tới
                client_mess = conn.recv(4096)
                if not client_mess: continue
                client_mess_string = client_mess.decode('utf-8')
                req = HttpRequest()
                req.parse_request(client_mess_string)
                req.print_parsed_request()
            
                respone_byte = router.route(req)
                print(respone_byte.decode('utf-8'))
                # Gửi message tới Client
                time.sleep(5) #Mô phỏng thời gian Server xử lý 1 Client request
                conn.sendall(respone_byte)
                # conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from Prism Auth Gateway")
    except Exception as e: 
        print(f"Gặp lỗi {e}")
    finally:
        print("Ngắt kết nối")

