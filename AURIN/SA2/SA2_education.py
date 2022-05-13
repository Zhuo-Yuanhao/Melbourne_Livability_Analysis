import json
with open("SA2_education_raw.json",'r') as load_f:
    edu_dic=json.load(load_f)
dicList=edu_dic['features']
dic={}
for i in range(len(dicList)):
    name=dicList[i]['properties']['sa2_name16']
    total=dicList[i]['properties']['tot_p']
    educated=dicList[i]['properties']['high_yr_schl_comp_yr_12_eq_p']
    if total==0:
        continue
    percentage=educated/total
    dic[name]=percentage
with open("SA2_education.json",'w') as json_file:
    json.dump(dic,json_file)

