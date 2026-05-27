
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
        header_Lines = Header_Request.split("\r\n")
        # Tách dòng đầu của Header lấy method, path, version
        request_Line = header_Lines[0].split(" ") 
        parts_request = request_Line[:3] # Copy 3 phần tử của request Line đề phòng gửi dư
        while len(parts_request) < 3: # Thêm Unknown vào nếu thiếu
            parts_request.append("UNKNOWN")
        self.method, self.path, self.version = parts_request
      
        # Tách key và value của từng dòng Headers
        for i in range(1,len(header_Lines)):
            if not header_Lines[i].strip():
                continue
            pos_split = header_Lines[i].find(":")
            if pos_split == -1:
                continue
            key = header_Lines[i][:pos_split].lower().strip()
            value = header_Lines[i][pos_split + 1:].strip()
            self.headers[key] = value

    def print_parsed_request(self):
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

        




