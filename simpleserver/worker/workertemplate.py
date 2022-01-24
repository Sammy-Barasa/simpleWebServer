from threading import Thread
class WorkerClass(Thread):
    def __init__(self,con,config):
        self.con = con
        self.config = config
        self.req = None        

    # processes requesti
    def process_req(self):
        if self.config["proxy"]:
            proxy_host = self.config["proxy"]["host"]
            proxy_port = self.config["proxy"]["port"]
            while True:
                try:
                    self.con.connect((proxy_host,proxy_host))
                    print(f"Proxy to {proxy_host},{proxy_port}")
                except TimeoutError as e:
                    print(e)
                    break
                except BaseException as err:
                    print(f"Unexpected {err=}, {type(err)=}")
                    raise
                    break
        request  = self.con.recv(1024).decode()
        self.req =request
        print(request)

        chunks = []
        while True:
            # Keep reading while the client is writing.
            data = self.con.recv(2048)
            if not data:
                # Client is done with sending.
                break
            chunks.append(data)
        self.req = b''.join(chunks).decode()
        print(self.req)
    def run(self):
        self.process_req()  
    # get request header

        # content type
        # content legth

    # get request body

    # get request path and params


    # def worker process returns: content-type,content-length,body,path,q params


    # def send a response given the decided response from server


    # print("SSL established. Peer: {}".format(conn.getpeercert()))



    