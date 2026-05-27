
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
        request_values = [self.method, self.path, self.version]
        if len(request_Line == len(request_values)): # Nếu request Line đủ cho 3 giá trị method, path, version
            request_values = request_Line
        else:
            # Gán các giá trị có từ request Line vào
            index = 0
            for i in range(len(request_Line)):
                request_values[i] = request_Line[i]
                index += 1
            # Còn thiếu giá trị nào thì gán "UNKNOWN"
            while (index < len(request_values)):
                request_values[index] = "UNKNOWN"
                index += 1
        self.method, self.path, self.version = request_Line.split(" ")
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

        




