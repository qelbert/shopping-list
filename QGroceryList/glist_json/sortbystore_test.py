import itertools
import json

with open('stores.json', 'r') as fp:
    stores = json.load(fp)
    print(json.dumps(stores, indent=2))

slist = ["chicken broth", "chicken tenders", "whole wheat spaghetti noodles", "celery"]
storelist = []

for ing2 in slist:
    y = stores[ing2][0]
    for k, v in y.items():
        if k in storelist : continue
        storelist.append(k)

for storenames in storelist :
    thisstore = []
    #print(storenames)
    for ing2 in slist:
        y = stores[ing2][0]
        for k, v in y.items():
            if k == storenames :
                thisstore.append(ing2)
    print(storenames)
    print(str(thisstore) + "\n\n")
