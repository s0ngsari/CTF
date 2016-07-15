from socket import *
from telnetlib import *

HOST = "cgc.cykor.kr"
PORT = 31324

def recvuntil(t):
        data = ''
        while not data.endswith(t):
                tmp = s.recv(1)
                if not tmp: break
                data += tmp
        return data

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))

payload = open("cykor1.xml","rb").read()
print recvuntil("What type of your PoV? (BIN / XML)")
s.send("XML\n")
print recvuntil("How many bytes is your XML?")
s.send("671\n")
print recvuntil("Ok.... send it :)")
print len(payload)
s.send(payload + "\n")

t = Telnet()
t.sock = s
t.interact()