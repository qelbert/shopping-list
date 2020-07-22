import json

with open('recipes.json', 'r') as fp:
    recipes = json.load(fp)
title = input("What is the name of your recipe?")
ingredients = []
ingredient = None

while True :
    ingredient = input("please type in ingredients one by one. When done, type 'end'.")
    if ingredient == "end" :
        break
    if ingredient in ingredients :
        print ("that ingredient is already in your list")
        continue
    ingredients.append(ingredient)
    if title not in recipes :
        recipes.setdefault(title,[]).append(ingredient)
    else : recipes[title].append(ingredient)
    print (title , "ingredients :" , ingredients)
with open('recipes.json', 'w') as fp:
    json.dump(recipes, fp)
print ("Your Recipe Collection includes the following: ==> ")
print(json.dumps(recipes, indent=2))
