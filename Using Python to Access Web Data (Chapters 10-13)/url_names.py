from urllib.request import urlopen
import urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) == 0:
    url = 'http://py4e-data.dr-chuck.net/known_by_Lennix.html'
count = int(input('Enter count: '))
pos = int(input('Enter position: ')) - 1
name = None
for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos].get('href', None)
    name = tags[pos].contents[0]
print(name)
