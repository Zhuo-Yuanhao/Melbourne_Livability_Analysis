import json
with open("SA2_psychological_raw.json",'r') as load_f:
    psy_dic=json.load(load_f)
dicList=psy_dic['features']
dic={}

for i in range(len(dicList)):
    name=dicList[i]['properties']['area_name']
    index=dicList[i]['properties']['k10_me_2_rate_3_11_7_13']
    if name=='Sydney (C)':
        dic['Sydney']=index
    elif name=='Adelaide (C)':
        dic['Adelaide']=index
    elif name=='Brisbane (C)':
        dic['Brisbane']=index
    elif name=='Melbourne (C)':
        dic['Melbourne']=index

with open("SA2_psychological.json",'w') as json_file:
    json.dump(dic,json_file)