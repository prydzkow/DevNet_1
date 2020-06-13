#pip install --upgrade pip
#pip install pyaml
import yaml

#open the YAML file
data = open('sampleFILE.yaml')

parsed_data = yaml.load(data, Loader=yaml.FullLoader)
#print(parsed_data)
#print(type(parsed_data))
#print(parsed_data['breakfast_menu'])
#print(type(parsed_data['breakfast_menu']))
#print(parsed_data['breakfast_menu']['food'])
#print(type(parsed_data['breakfast_menu']['food']))

#print the data for each food
#for i in parsed_data['breakfast_menu']['food']:
#    print(i)
#    print(type(i))

data.close()
