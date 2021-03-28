import socket
from socketserver import BaseRequestHandler, TCPServer

class TCPHandler(BaseRequestHandler):
  def handle(self):
    data = self.request.recv(1024).strip()
    print(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect(('ilt.learn.mulesoft.com', 80))
      sock.sendall(data)

      data = sock.recv(4096)
      print(data)

      self.request.sendall(data)

if __name__ == '__main__':
  with TCPServer(('localhost', 8888), TCPHandler) as server:
    server.serve_forever()