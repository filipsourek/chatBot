import socket, sys

IP = "194.233.160.94"

PORT = 5555 
HEADERSIZE = 5

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.status = "Disconected"
        try:  
            self.client.connect((IP,PORT)) 
            self.status = "Connected"
            
        except socket.error:
            self.status = "Disconected"
    def send_msg(self, msg):
        if msg:
            msg = msg.encode()
            msg_head = f"{len(msg):<{HEADERSIZE}}".encode()
            try:
                self.client.send(msg_head + msg)     
            except socket.error:
                self.status = "Disconected"
    def recv_msg(self):
        header = self.client.recv(HEADERSIZE)
        if not len(header):
            sys.exit()
        lenght = int(header.decode().strip())
        msg = self.client.recv(lenght).decode()
        return(msg)
