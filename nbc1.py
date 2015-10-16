import urllib.request
from http import cookiejar
from urllib.parse import urlencode

jar = cookiejar.CookieJar()

credentials = {'user': 'neriki', 'passwrd': 'password', 'cookielength' : '-1'}
credenc = urlencode(credentials).encode('ascii')

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
urllib.request.install_opener(opener)

req = opener.open('https://www.newbiecontest.org/forums/index.php?action=login2', credenc)
test = opener.open('https://www.newbiecontest.org/epreuves/prog/prog1.php')
#print(req.read())

v=str(test.read()).split(':')[1].replace('\'','').strip()

print(v)

test2 = opener.open('https://www.newbiecontest.org/epreuves/prog/verifpr1.php?solution='+ v)

print(test2.read())
