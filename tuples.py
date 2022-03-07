import pandas as pd
import requests
import json
from flatten_json import flatten
import re

#making a list of id
id=requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects')
id=json.loads(id.content)
id=id["objectIDs"]

a=[]
for i in id[:10]:

    object = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(i))
    object = json.loads(object.content)
    fdata=flatten(object)
    a.append(fdata)



df=pd.json_normalize(a)

x=df.columns.values.tolist()
print(x)
for i in range(len(x)):
    x[i]=re.sub("_[0-9]_","_",x[i])
#    x[i]=re.sub("__","_",x[i])
print(x)


final=df.to_csv('museum1.csv',encoding='utf-8-SIG', header=x, index=False)









