import json
import pandas as pd

name=[]
value=[]
with open('./new_json_media.json','r',encoding='utf-8') as f:
    data=json.load(f)
    for i in range(len(data)):
        name.append(data[i]['name'])
        value.append(data[i]['value'])

df=pd.DataFrame({'name':name,'value':value})
df.to_csv("2022-03-01_media.csv",index=False,sep=',')
a=pd.read_csv("2022-03-01_media.csv")
print(a)