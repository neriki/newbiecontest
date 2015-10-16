import urllib.request
from http import cookiejar
from urllib.parse import urlencode
import math

jar = cookiejar.CookieJar()

credentials = {'user': 'neriki', 'passwrd': 'heremypass', 'cookielength' : '-1'}
credenc = urlencode(credentials).encode('ascii')

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
urllib.request.install_opener(opener)

req = opener.open('https://www.newbiecontest.org/forums/index.php?action=login2', credenc)

reqa = opener.open('https://www.newbiecontest.org/epreuves/prog/prog3_1.php')
a=int(str(reqa.read()).split(':')[1].replace('\'','').strip())

reqb = opener.open('https://www.newbiecontest.org/epreuves/prog/prog3_2.php')
b=int(str(reqb.read()).split(':')[1].replace('\'','').strip())

test2 = opener.open('https://www.newbiecontest.org/epreuves/prog/verifpr3.php?solution='+ str(int(math.sqrt(a)*b)))

print(test2.read())
