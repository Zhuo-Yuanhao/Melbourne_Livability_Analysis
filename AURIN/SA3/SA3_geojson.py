import json
import geojson
from geojson import Feature, Polygon, FeatureCollection

with open("SA3_education.json",'r') as load_f:
    edu_dic=json.load(load_f)
with open("SA3_foreigner.json",'r') as load_f:
    for_dic=json.load(load_f)
with open("SA3_psychological.json",'r') as load_f:
    psy_dic=json.load(load_f)
MelPoint=Polygon([[(144.593742, -38.433859), (144.593742, -37.511274), (145.512529, -37.511274), (145.512529, -38.433859)]])
SydPoint=Polygon([[(150.520929, -34.118347), (150.520929, -33.578141), (151.343021, -33.578141), (151.343021, -34.118347)]])
AdlPoint=Polygon([[(138.44213, -35.34897), (138.44213,-34.652564), (138.78019, -34.652564), (138.78019, -35.34897)]])
BriPoint=Polygon([[(152.668523, -27.767441), (152.668523, -26.996845), (153.31787, -26.996845), (153.31787, -27.767441)]])
MelFeature=Feature(geometry=MelPoint, properties={"city_name":"Melbourne","education_rate":edu_dic['Melbourne'],"foreiner_percetage":for_dic['Melbourne'],"psycho_health":psy_dic['Melbourne']})
SydFeature=Feature(geometry=SydPoint, properties={"city_name":"Sydney","education_rate":edu_dic['Sydney'],"foreiner_percetage":for_dic['Sydney'],"psycho_health":psy_dic['Sydney']})
AdlFeature=Feature(geometry=AdlPoint, properties={"city_name":"Adelaide","education_rate":edu_dic['Adelaide'],"foreiner_percetage":for_dic['Adelaide'],"psycho_health":psy_dic['Adelaide']})
BriFeature=Feature(geometry=BriPoint, properties={"city_name":"Brisbane","education_rate":edu_dic['Brisbane'],"foreiner_percetage":for_dic['Brisbane'],"psycho_health":psy_dic['Brisbane']})
feature_collection = FeatureCollection([MelFeature, SydFeature,BriFeature,AdlFeature])
with open("SA3_geojson.geojson",'w') as f:
    geojson.dump(feature_collection,f)