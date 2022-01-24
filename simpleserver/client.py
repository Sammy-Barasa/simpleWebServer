from http import client
import socket
import string
import ssl

secure = False
if secure:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,client)
    s.connect(('localhost', 3000))
    s.sendall(b'Hello secure erver')
    s=ssl.wrap_socket(s,server_side=False)
    s.close()
    # sslSocket = socket.ssl(s)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3000))
s.sendall(b'Hello secure erver')
# sslSocket = socket.ssl(s)
s.close()



# conn = ssl.wrap_socket(socket.socket(socket.AF_INET),
                            # server_hostname="localhost")
# conn.connect(("www.python.org", 443))

# conn.write('Hello secure socket\n')
# conn.close()