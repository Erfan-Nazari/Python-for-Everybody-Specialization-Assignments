import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) != 0:
    xm = urlopen(url, context=ctx).read()
else :
    xm = urlopen('http://py4e-data.dr-chuck.net/comments_1870302.xml', context=ctx).read()
tree = ET.fromstring(xm)
#counts = tree.findall('comments/comment/count')
counts = tree.findall('.//count')
icounts = [int(count.text) for count in counts]
print(sum(icounts))