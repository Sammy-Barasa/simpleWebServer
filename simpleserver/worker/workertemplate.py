class Worker():
    def __init__(self,con,):
        self.con = con
        self.req = None        

    def process_req(self):
        request  = self.con.recv(1024).decode()
        self.req =request
        print(request)