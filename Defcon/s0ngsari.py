from socket import *
import struct,time
from ctypes import *
from telnetlib import *


p32 = lambda x:struct.pack("<L",x)
up32 = lambda x:struct.unpack("<L",x)
p64 = lambda x:struct.pack("<Q",x)
up64 = lambda x:struct.unpack("<Q",x)



def recvuntil(t):
        data = ''
        while not data.endswith(t):
                tmp = s.recv(1)
                if not tmp: break
                data += tmp
        return data





