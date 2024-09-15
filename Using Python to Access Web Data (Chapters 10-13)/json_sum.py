import urllib.request
from urllib.request import urlopen
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) != 0:
    xm = urllib.request.urlopen(url, context=ctx).read()
else :
    js = urlopen('http://py4e-data.dr-chuck.net/comments_1870303.json', context=ctx).read().decode()
data = json.loads(js)
total = 0
for item in data['comments']:
    total = total + item['count']
print(total)