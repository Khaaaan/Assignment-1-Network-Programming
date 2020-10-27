import datetime
import socket
import argparse
import random


MAX_BYTES = 65535




class Server:


    def __init__(self,interface,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((interface,port))
        print(f'Listening at {self.sock.getsockname()}')
        self.receive()

    def receive(self):
        while True:
            self.data, self.address = self.sock.recvfrom(MAX_BYTES)
            if random.random() < 0.5:
                print(f'Pretending to drop packet {self.address}')
                continue
            self.text = self.data.decode('ascii')
            print(f'The client at {self.address} says {self.text}')
            # Respond to the sender of the packet
            self.message = f'Your data was {len(data)} bytes long'
            self.sock.sendto(self.message.encode('ascii'), self.address)
            

        


class Client:

    def __init__(self, hostname, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((hostname, port))
        print(f'Client socket name is {self.sock.getsockname()}')
        self.send()

    def send(self):
        self.time = datetime.datetime.now().time()

        if (datetime.time(12,0,0)<= self.time < datetime.time(17,0,0)):
            self.maxDelay = 2
            self.k = 2
        elif (datetime.time(17,0,0)<= self.time < datetime.time(23,59,0)):
            self.maxDelay = 4
            self.k = 3
        else:
            self.maxDelay = 1
            self.k = 2

        self.delay = 0.1

        self.text = "This is another message"
        self.data = self.text.encode('ascii')

        while True:
            self.sock.send(self.data)
            print(f'Waiting up to {round(self.delay,2)} seconds for a reply')
            self.sock.settimeout(self.delay)
            try: 
                self.data = self.sock.recv(MAX_BYTES)
            except:
                self.delay *= self.k
                if self.delay > self.maxDelay:
                    raise RuntimeError('I think the server is down')
            
            else:
                break 
        print(f"The server says {self.data.decode('ascii')}")


if __name__ == '__main__':
    choices = {'client': Client, 'server': Server}
    parser = argparse.ArgumentParser(description='Send and receive UDP,'
                                                        ' pretending packets are often dropped')
    parser.add_argument('role', help='which role to take')
    parser.add_argument('host', help='interface the server listens at; host the client sends to')
    parser.add_argument('-p',type =int,default=1060, help='UDP port (default 1060)')

    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
    