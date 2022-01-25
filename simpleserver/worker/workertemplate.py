from threading import Thread



class WorkerClass(Thread):
    def __init__(self,con=None,config={}):
        Thread.__init__(self)
        self.con = con
        self.config = config
        self.req = None        

    # processes requesti

    def decode_req(self,client_connection):
          
        "GET / HTTP/1.1"
        reqst  = client_connection.recv(1024)
        self.req =reqst.decode()
        # chunks = []
        # while True:
        #     # Keep reading while the c
        #     # lient is writing.
        #     data = connetn.recv(1024)
        #     if not data:
        #         # Client is done with sending.
        #         break
        #     chunks.append(data)
        # print(chunks)
        # self.req = b''.join(chunks).decode()
        
        # print(req)
        print(self.req)
        
        # "GET /index.html HTTP/1.1"
        resp =  b"HTTP/1.1 200 OK\n\nHello World"
        client_connection.send(resp)
        # self.req=None
        # client_connection.close()
        print("response sent")
        self.req=None
        "POST /form.php HTTP/1.1"
        "Content-Type: application/json"
        "Content-Length: 21"
        resp =  b"HTTP/1.1 200 OK\n\nHello World"
        client_connection.send(resp)
        # cgitb.enable()
        return        
    

    def process_req(self):

        # no ssl
        if not(self.config["http"]["ssl/tls"]):
            self.decode_req(self.con)
        
        # no ssl and proxy
        elif not(self.config["http"]["ssl/tls"]) and 'proxy' in self.config["server"]:
            proxy_host = self.config["server"]["proxy"]["host"]
            proxy_port = self.config["server"]["proxy"]["port"]
            while True:
                try:
                    self.con.connect((proxy_host,proxy_port))
                    print(f"Proxy to {proxy_host},{proxy_port}")
                except TimeoutError as e:
                    print(e)
                    self.con.close()
                    break
                except BaseException as err:
                    self.con.close()
                    print(f"Unexpected {err=}, {type(err)=}")
                    raise
        #  ssl no proxy
        elif self.config["http"]["ssl/tls"] and 'proxy' not in self.config["server"]:
            self.decode_req(self.con)

        # ssl has proxy, suitable for localhost proxy
        elif 'proxy' in self.config["server"] and self.config["http"]["ssl/tls"]:
            proxy_host = self.config["server"]["proxy"]["host"]
            proxy_port = self.config["server"]["proxy"]["port"]
            while True:
                try:
                    self.con.connect((proxy_host,proxy_port))
                    print(f"Proxy to {proxy_host},{proxy_port}")
                except TimeoutError as e:
                    print(e)
                    self.con.close()
                    break
                except BaseException as err:
                    self.con.close()
                    print(f"Unexpected {err=}, {type(err)=}")
                    raise

        # ssl only
        else:
            self.decode_req(self.con)        
        
    def run(self):
        try:
            self.process_req()
            
        except BaseException:
            raise
          
    # get request header

        # content type
        # content legth

    # get request body

    # get request path and params


    # def worker process returns: content-type,content-length,body,path,q params


    # def send a response given the decided response from server


    # print("SSL established. Peer: {}".format(conn.getpeercert()))



    