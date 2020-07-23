import json
from pprint import pprint
f = open('sampleFILE.json')
data = json.load(f)

#imported as Python dictionary
#print(data)
#print(type(data))

#print the data for each food
#for i in data['breakfast_menu']['food']:
#    print(i)
#    print(type(i))

#print(data['breakfast_menu'])
#print(type(data['breakfast_menu']['food']))

new_json = json.dumps(data)
print(new_json)
print(type(new_json))

f.close()