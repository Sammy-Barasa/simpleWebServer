import ssl, socket, os
from threading import Thread
from worker.workertemplate import WorkerClass 
import sys

class ThreadedServer(Thread):
    def __init__(self,config={},set_up_complete=False,base_dir =""):
        self.conf = config
        self.port = config["server"]["port"]
        self.hostname= config["server"]["host"]
        self.ssl_tls = config["http"]["ssl/tls"]
        self.setup_up_complete = set_up_complete
        self.dirbase = base_dir
        self.server_state = False
    

    def run(self):
        
        sock = None
        # creating socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.ssl_tls:
            # creating secure transport layer supporting HTTPS
            print("Creating a secure communication layer..")
            try:
                sock = ssl.wrap_socket(serversocket,certfile=os.path.join(self.dirbase,"cert.pem"),keyfile=os.path.join(self.dirbase,"key.pem"),server_side=True)
                print("Created a secure communication layer") 
            except BaseException as g:
                print(type(g))
                print(g)
                self.ssl_tls =False
                return self.run() # incase off error do http
            except:
                print("Creating a non-secure http communication layer ...")
                sock = ssl.wrap_socket(serversocket, cert_reqs=ssl.CERT_NONE,certfile=os.path.join(self.dirbase,"cert.pem"),keyfile=os.path.join(self.dirbase,"key.pem"),
                                 server_side=True)
    
        else:                          
            # creating channel supporting HTTP
            print("Creating a non-secure http communication layer ....")
            print("Created a non-secure http communication layer")
            sock = serversocket
        print(self.hostname)
        print(self.port)
        sock.bind((self.hostname,self.port))
                
        sock.listen(5)
        self.server_state = True
        
        print(f"simpleWebServer listening on port {self.port}")
        # sock.close()
        while True:
            try:
                if self.server_state:
                    print("simpleWebServer is LIVE!")
                    print("Press ctrl+c to exit!!!")
                    # check if set_up_complete and config_has_not_changed
                    (client_conn,address) = sock.accept()
                    while client_conn:
                        print(f"New connection from {address} ")
                        webworker = WorkerClass(con=client_conn,config=self.conf)
                        # webworker.setDaemon(True)
                        # webworker.start()
                        webworker.run()
                        client_conn.close()
                        
                # lsof -l -nping -c 3 127.0.0.1
                # https://www.programcreek.com/python/example/1124/ssl.wrap_socket
                # https://realpython.com/python-sockets/
                # print("simpleWebServer is STOPPED!")
                # continue
            except KeyboardInterrupt:
                # if ctrl + c? close connection,quit
                # if keyboard.is_pressed('ctrl+c'):
                sock.close()
                self.server_state = False
                print("\nYou pressed ctrl+c")
                print("exiting ....")
                print("Exitted!!!")
                sys.exit(1)
                # break 
                # if ctrl + r? close connection, quit, run python3 main.py reload
                
                # sock.close()
            except OSError:
                sock.close()
                self.server_state = False
                raise 
                
            # finally:
            #     self.server_state = False
            #     sock.close()
            #     sys.exit(1)