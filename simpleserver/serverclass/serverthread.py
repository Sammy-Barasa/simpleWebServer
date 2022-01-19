import ssl, socket, os
from threading import Thread
from worker.workertemplate import Worker 
from main import BASE_DIR

class ThreadedServer(Thread):
    def __init__(self,config={}):
        self.port = config["port"]
        self.hostname= config["host"]

    def run(self):
        # creating socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        serversocket.bind((self.hostname,self.port))
        serversocket.listen(5)
        
        print(f"listening on port {self.port}")

        
        sock = ssl.wrap_socket(serversocket,
                                keyfile=os.path.join(BASE_DIR,"key.pem"),
                                certfile=os.path.join(BASE_DIR,"cert.pem"), server_side=True)

        while True:
            (client_conn,address) = sock.accept()

            webworker = Worker(client_conn)