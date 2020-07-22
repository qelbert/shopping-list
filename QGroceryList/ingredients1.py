import json

#Open json dictionary to (r)ead through
with open('recipes.json', 'r') as fp:
    recipes = json.load(fp)

ingredients = []
for k,v in recipes.items() :
    for x in v :
        if x in ingredients : continue
        ingredients.append(x)
print(ingredients)
