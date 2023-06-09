from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#ht = list()
url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
x = list()
for l in range(count):
    print('Retrieving: ',url)
    x.append(re.findall('http://.*_(.+).html',url))

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    index = 0
    for tag in tags:
        index+=1
        if index == pos:
            url = tag.get('href', None )
            break
