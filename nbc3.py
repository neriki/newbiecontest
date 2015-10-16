import urllib.request
from http import cookiejar
from urllib.parse import urlencode
import datetime
import math

jar = cookiejar.CookieJar()

credentials = {'user': 'neriki', 'passwrd': 'heremypass', 'cookielength' : '-1'}
credenc = urlencode(credentials).encode('ascii')

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
urllib.request.install_opener(opener)

req = opener.open('https://www.newbiecontest.org/forums/index.php?action=login2', credenc)

print(datetime.datetime.time(datetime.datetime.now()))
reqq = opener.open('https://www.newbiecontest.org/epreuves/prog/prog4.php')

q=str(reqq.read())

a=int(q.split('(')[1].split(')')[0])
b=int(q.split('*')[1].split('&')[0])
c=int(q.split('+')[1].split(' ')[0])

print (str(a) + " " + str(b) + " " + str(c))
print(str(int(math.sqrt(a)*(b*b)+c)))

test2 = opener.open('https://www.newbiecontest.org/epreuves/prog/verifpr4.php?solution='+ str(int(math.sqrt(a)*(b*b)+c)))
print(datetime.datetime.time(datetime.datetime.now()))
print(test2.read())
