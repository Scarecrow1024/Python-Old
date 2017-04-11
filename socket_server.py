import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} worte".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print('error', e)
                break

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('localhost', 6969), MyServer)
    server.serve_forever()