from sys import stdin, stdout
import getpass
import telnetlib
from collections import deque

class TelnetClient:
    def __init__(self, host, port=23):
        self.host = host
        self.port = port

#    def connect(self):
#        self.tn = telnetlib.Telnet(self.host, self.port)
#        self.history = deque([])
    def __enter__(self):
        self.tn = telnetlib.Telnet(self.host, self.port)
        self.history = deque([])

#    def cleanup(self):
#        self.tn.close()
#        self.tn = None
#
#        with open('history.txt', 'a') as f:
#            f.writelienes(self.history)
    def __exit_(self, exc_type, exc_value, exc_tb):
        self.tn.close()
        self.tn = None

        with open('history.txt', 'a') as f:
            f.writelienes(self.history)

    def login(self):
        # user
        self.tn.read_until(b"login: ")
        user = input("Enter your remote account: ")
        self.tn.write(user.encode('utf8') + b'\n')

        # password
        self.tn.read_until(b'Password: ')
        password = getpass.getpass()
        self.tn.write(password.encode('utf8') + b'\n')
        out = self.tn.read_until(b'$ ')
        stdout.write(out.decode('utf8'))

    def interact(self):
        while True:
            cmd = stdin.readline()
            if not cmd:
                break

        self.history.append(cmd)
        self.tn.write(cmd.encode('utf8'))
        out = self.tn.read_until(b'$ ').decode('utf8')

        stdout.write(out[len(cmd)+1:])
        stdout.flush()


#client = TelnetClient('192.168.0.105')
#client.connect()
#client.login()
#client.interact()
#client.cleanup()

with TelnetClient('192.168.0.105') as client:
    client.login()
    client.interact()

print('END')
