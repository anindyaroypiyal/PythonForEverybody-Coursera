import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx).read()

    print('Retrieved', len(uh), 'characters')

    sum = 0
    c = 0
    tree = ET.fromstring(uh)

    counts = tree.findall('.//count')
    print('Count:', len(counts))
    for item in counts:
        sum += int(item.text)
    print('Sum:',sum)
