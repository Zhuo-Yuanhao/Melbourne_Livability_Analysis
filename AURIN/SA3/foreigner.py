import json
with open("SA3_foreigner_raw.json",'r') as load_f:
    for_dic=json.load(load_f)
dicList=for_dic['features']
dic={}

for i in range(len(dicList)):
    name=dicList[i]['properties']['lga_name18']
    percentage=dicList[i]['properties']['citizenship_status_p_brn_ovs_aus_citizen_pr100']
    if name=='Sydney (C)':
        dic['Sydney']=percentage
    elif name=='Adelaide (C)':
        dic['Adelaide']=percentage
    elif name=='Brisbane (C)':
        dic['Brisbane']=percentage
    elif name=='Melbourne (C)':
        dic['Melbourne']=percentage
with open("SA3_foreigner.json",'w') as json_file:
    json.dump(dic,json_file)