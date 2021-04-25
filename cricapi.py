import urllib.request as url
import json

res = url.urlopen('https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=253802')
data = json.load(res)

print(data['profile'])
odi = data['data']['batting']['ODIs']
print(odi)
