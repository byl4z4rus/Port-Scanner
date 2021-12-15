import socket 

class Scanning:

    def __init__(self):
        pass
    
    def set(self, ipaddress, port_range):
        
        self.ipaddress = ipaddress
        self.port_range = port_range

    def scan_port(self):
        start_port, end_port = self.port_range.split("-")
        
        for i in range(int(start_port), int(end_port)):
            try:   
                sock=socket.socket()
                sock.settimeout(0.2)
                sock.connect((self.ipaddress,i))
                print(f"port {i} is open")
            except:
                print(f"port {i} is close")