import json
f = open('sampleFILE.json')
data = json.load(f)

#imported as Python dictionary
#print(data)
#print(type(data))

#print the data for each food
#for i in data['breakfast_menu']['food']:
#    print(i)

f.close()