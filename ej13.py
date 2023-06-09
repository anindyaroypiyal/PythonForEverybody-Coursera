import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter location: ')
print('Retrieving',url )
connection = urllib.request.urlopen(url)
data = connection.read().decode()

info = json.loads(data)
print('Retrieved', len(data),'characters')

c = 0
sum = 0

for x in info['comments']:
    c+=1
    
    sum += x['count']

print('Count: ',c)
print('Sum: ',sum)
