import socket 

HOST = '127.0.0.1'
PORT = 8080

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
                client_mess = conn.recv(1024)
                if not client_mess: break
                print(f"Message mà client gửi tới: {client_mess.decode('utf-8')}")
                conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from Prism Auth Gateway")
    except Exception as e: 
        print(f"Gặp lỗi {e}")
    finally:
        print("Ngắt kết nối")

