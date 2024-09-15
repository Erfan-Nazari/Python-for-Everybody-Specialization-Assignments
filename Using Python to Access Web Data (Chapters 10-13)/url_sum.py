from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) != 0:
    html = urlopen(url, context=ctx).read()
else :
    html = urlopen('http://py4e-data.dr-chuck.net/comments_1870300.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
total = 0
for tag in tags:
    total = total + int(tag.contents[0])
print(total)
    