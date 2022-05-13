import json
with open("SA2_population2016_raw.json",'r') as load_f:
    for_dic=json.load(load_f)
dicList=for_dic['features']
dic={}
for i in range(len(dicList)):
    name=dicList[i]['properties']['sa2_name_2016']
    percentage=dicList[i]['properties']['australian_citizenship_census_not_an_australian_citizen_pc']
    dic[name] = percentage
with open("SA2_population.json",'w') as json_file:
    json.dump(dic,json_file)