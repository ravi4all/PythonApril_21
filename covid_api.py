import urllib.request as url
import json

res = url.urlopen('https://api.covid19india.org/states_daily.json')
data = json.load(res)

states = data['states_daily']
state = 'dl'
conf_cases = []
for i in range(len(states)):
    if states[i]['status'] == 'Confirmed':
        conf_cases.append(states[i])

death_cases = []
for i in range(len(states)):
    if states[i]['status'] == 'Deceased':
        death_cases.append(states[i])

rec_cases = []
for i in range(len(states)):
    if states[i]['status'] == 'Recovered':
        rec_cases.append(states[i])


sum = 0
for i in range(len(conf_cases)):
    sum += int(conf_cases[i][state])

print("Delhi Total Confirmed Cases Till Date :",sum)

sum = 0
for i in range(len(rec_cases)):
    sum += int(rec_cases[i][state])

print("Delhi Total Recovered Cases Till Date :",sum)

sum = 0
for i in range(len(death_cases)):
    sum += int(death_cases[i][state])

print("Delhi Total Deceased Cases Till Date :",sum)
