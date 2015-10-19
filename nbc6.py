import urllib.request
from http import cookiejar
from urllib.parse import urlencode
import datetime
import math

jar = cookiejar.CookieJar()

credentials = {'user': 'neriki', 'passwrd': 'abcd1234!', 'cookielength' : '-1'}
credenc = urlencode(credentials).encode('ascii')

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
urllib.request.install_opener(opener)

req = opener.open('https://www.newbiecontest.org/forums/index.php?action=login2', credenc)

reqq = opener.open('https://www.newbiecontest.org/epreuves/prog/prog6.php')

q=str(reqq.read())

q=q.split(':')[1].replace('<br />', '')

print(q)

a=int(q.split('x')[0].replace(' ', ''))

b=int(q.split('x')[3].replace('b2','').replace(' ', ''))

q=q.split('x')[4].split('=')

if q[0] !=' ':
	c=int(q[0].replace(' ', ''))
else:
	c=0
y=int(q[1].replace('"','').replace(' ', ''))

print(a)
print(b)
print(c)
print(y)

x1 = (-b + math.sqrt((b*b)- (4 *a *c))) / (2*a)
x2 = (-b - math.sqrt((b*b)- (4 *a *c))) / (2*a)

if x1>x2:
	x=x1
else:
	x=x2

print(x)

print(str(x)[:len(str(x).split('.')[0])+3])
test2 = opener.open('https://www.newbiecontest.org/epreuves/prog/verifpr6.php?solution='+ str("%.2f" % x))

print(test2.read())
