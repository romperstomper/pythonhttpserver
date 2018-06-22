import os
import re
import socket

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
        headers = {}
        while True:
            line = self.read_line()
            if not line: break
            print "line: ", line
            key, value = re.split(r':\s', line)
            headers[key] = value

        return method, path, version, headers

if __name__ == '__main__':
    main()
