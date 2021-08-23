# CHARON
# socket program for creating server on port 5050 for chatting in tcp connection with client

from socket import *

s = socket(AF_INET , SOCK_STREAM)

server = "0.0.0.0"

port = 5050

ADDR = (server,port)

s.bind((ADDR))

s.listen(5)

print("[+] server chat is running : ")

c , ADDR2 = s.accept()

print("[+] connected to %s \n" % str(ADDR2))

while True:

    sms = input("[+] you >> ")
    c.sendall(sms.encode('utf-8'))
    print("\n")
    data = c.recv(1024)
    print("[+] person >> %s " % data.decode('utf-8'))
    print("\n")

c.close()