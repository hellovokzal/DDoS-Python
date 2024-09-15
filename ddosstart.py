from os import *
system("pip install requests")
from requests import *
from threading import Thread

num = 0

def zaproc(getting):
    global num
    while True:
        get(getting)
    
link = input("Enter link: ")
    
print("started!")
    
while True:
    start = Thread(target=zaproc, args=(link,))
    start.start()
