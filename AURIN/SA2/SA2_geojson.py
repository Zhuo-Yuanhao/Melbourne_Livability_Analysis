import json
import geojson
from geojson import Feature, Polygon, FeatureCollection

with open("SA2_education.json",'r') as load_f:
    edu_dic=json.load(load_f)
with open("SA2_population.json",'r') as load_f:
    for_dic=json.load(load_f)
with open("SA2_psychologicaldistress.json",'r') as load_f:
    psy_dic=json.load(load_f)
with open("suburb_vic.geojson") as load_f:
    ref_dic=geojson.load(load_f)
with open("language.json") as load_f:
    ref2_dic=geojson.load(load_f)
ref=ref_dic["features"]
refDic={}
for i in range(len(ref)):
    name=ref[i]['properties']['vic_loca_2'].lower()
    polygon=ref[i]["geometry"]["coordinates"][0]
    refDic[name]=polygon
validList=[]
for key in ref2_dic:
    if (key in for_dic) and (key in edu_dic) and (key.lower() in refDic) and (key in psy_dic):
        validList.append(Feature(geometry=Polygon(refDic[key.lower()]),
                                 properties={"city_name":key,"education_rate":edu_dic[key],
                                             "foreiner_percetage":for_dic[key],"psycho_health":psy_dic[key]}))
feature_collection = FeatureCollection(validList)
with open("SA2_geojson.geojson",'w') as f:
    geojson.dump(feature_collection,f)
