import json

with open('recipes.json', 'r') as fp:
    recipes = json.load(fp)

print(json.dumps(recipes, indent=2))

print(json.dump(recipes, indent=4))
