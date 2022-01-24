import ssl, socket, os
from threading import Thread
from worker.workertemplate import WorkerClass 
import keyboard

class ThreadedServer(Thread):
    def __init__(self,config={},set_up_complete=False,base_dir =""):
        self.conf = config
        self.port = config["server"]["port"]
        self.hostname= config["server"]["host"]
        self.ssl_tls = config["http"]["ssl/tls"]
        self.setup_up_complete = set_up_complete
        self.dirbase = base_dir
    

    def run(self):
        print("reached here")
        sock = None
        # creating socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.ssl_tls:
            # creating secure transport layer supporting HTTPS
            print("Creating a secure communication layer")
            
            sock = ssl.wrap_socket(serversocket,certfile=os.path.join(self.dirbase,"cert.pem"),keyfile=os.path.join(self.dirbase,"key.pem"),
                                 server_side=True) 
                  
        else:                          
            # creating channel supporting HTTP
            print("Creating a http communication layer")
            sock = serversocket

        sock.bind((self.hostname,self.port))
        sock.listen(5)
        
        print(f"simpleWebServer listening on port {self.port}")
        # sock.close()
        while True:
            try:
                # check if set_up_complete and config_has_not_changed
                (client_conn,address) = sock.accept()
                
                
                while client_conn:
                    print(f"New connection from {address} ")
                    
                    webworker = WorkerClass(client_conn,self.conf)

                # lsof -l -nping -c 3 127.0.0.1
                # https://www.programcreek.com/python/example/1124/ssl.wrap_socket
                # https://realpython.com/python-sockets/
            except KeyboardInterrupt:
                # if ctrl + c? close connection,quit
                if keyboard.read_key() == "ctrl-c":
                    print("You pressed ctrl+c")
                    sock.close()
                    break 
                # if ctrl + r? close connection, quit, run python3 main.py reload
                if keyboard.read_key() == "ctrl-r":
                    print("You pressed ctrl+r")
                    sock.close()
                    
                    self.reload(self.can_reload)
                    # call reload function passing can reload state
                    break 
                sock.close()
            finally:
                sock.close()