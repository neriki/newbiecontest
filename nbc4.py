import urllib.request
from http import cookiejar
from urllib.parse import urlencode
import datetime
import string

clef=''

def decodeChar(ch):
	print(ch)
	ind=string.ascii_lowercase.index(ch)
	if ind>=clef:
		return string.ascii_lowercase[ind-clef]
	else:
		return string.ascii_lowercase[len(string.ascii_lowercase) - (clef - ind)]


jar = cookiejar.CookieJar()

credentials = {'user': 'neriki', 'passwrd': 'abcd1234!', 'cookielength' : '-1'}
credenc = urlencode(credentials).encode('ascii')

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
urllib.request.install_opener(opener)

req = opener.open('https://www.newbiecontest.org/forums/index.php?action=login2', credenc)

reqq = opener.open('https://www.newbiecontest.org/epreuves/prog/prog5.php')

q=str(reqq.read())
print(q)

phrase=q.split('\'')[1]
print(phrase)
clef=int(q.split('\'')[3])

phrase="".join(map (decodeChar,phrase))


print(phrase)
test2 = opener.open('https://www.newbiecontest.org/epreuves/prog/verifpr5.php?solution='+ phrase)

print(test2.read())
