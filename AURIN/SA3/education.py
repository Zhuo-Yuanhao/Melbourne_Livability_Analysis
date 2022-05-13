import json
with open("SA3_education_raw.json",'r') as load_f:
    edu_dic=json.load(load_f)
dicList=edu_dic['features']
dic={}
for i in range(len(dicList)):
    name=dicList[i]['properties']['sa2_name16']
    total=dicList[i]['properties']['p_aged_15_yr_over_p']
    none=dicList[i]['properties']['non_sc_quals_certtot_level_p']
    if name=='Sydney - Haymarket - The Rocks':
        dic['Sydney']=(total-none)/total
    elif name=='Adelaide':
        dic['Adelaide']=(total-none)/total
    elif name=='Brisbane City':
        dic['Brisbane']=(total-none)/total
    elif name=='Melbourne':
        dic['Melbourne']=(total-none)/total
with open("SA3_education.json",'w') as json_file:
    json.dump(dic,json_file)


