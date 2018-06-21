import socket
import os

def main():

    os.listdir(os.getcwd())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    addr = ('localhost', 9009)
    s.bind(addr)
    s.listen(0)

    conn_sock, addr_info = s.accept()
    #conn = Connection(conn_sock)
    conn = Connection(conn_sock)
    print conn.read_request()

class Connection(object):
    def __init__(self, conn_sock):
        self.conn_sock = conn_sock
        self.buffer = ''

    def read_line(self):
        while "\r\n" not in self.buffer:
            self.buffer += self.conn_sock.recv(7)
        result, self.buffer = self.buffer.split("\r\n", 2)
        return result

    def read_request(self):
        request_line = self.read_line()
        method, path, version = request_line.split(" ", 3)
        return method, path, version

if __name__ == '__main__':
    main()
