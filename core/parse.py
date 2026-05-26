
class HttpRequest:
    def __init__(self):
        self.method = ""
        self.path = ""
        self.version = ""
        self.body = ""
        self.headers = {}

    def parse_request(self, raw_data_string):
        pos = raw_data_string.find("\r\n\r\n") # tìm vị trí chia cụm header và body 
        if pos == -1:
            Header_Request = raw_data_string
            self.body = ""
        else:
            Header_Request = raw_data_string[:pos]
            self.body = raw_data_string[pos+4:]
        # Chia cách dòng của Header        
        header_Line = Header_Request.split("\r\n")
        # Tách dòng đầu của Header lấy method, path, version
        request_Line = header_Line[0]
        self.method, self.path, self.version = request_Line.split(" ")
        # Tách key và value của từng dòng Headers
        for i in range(1,len(header_Line)):
            pos_split = header_Line[i].find(":")
            key = header_Line[i][:pos_split].lower().strip()
            value = header_Line[i][pos_split + 1:].strip()
            self.headers[key] = value

    def print_paresed_request(self):
        print("\n--- [PRISM PARSED LOG] ---")
        print(f"Method : {self.method}")
        print(f"Path : {self.path}")
        print(f"Version: {self.version}")
        print("Header: ")
        for key, value in self.headers.items():
            print(f" --- {key} : {value}")
        if self.body:
            print(f"Body: {self.body}")
        print("=========")

        




