#if adding new recipe

title = input("What is the name of your recipe?")
recipes = dict()
ingredients = []
ingredient = None

while ingredient != "end" :
    ingredient = input("please type in ingredients one by one. When done, type 'end'.")
    if ingredient in ingredients :
        print ("that ingredient is already in your list")
        continue
    ingredients.append(ingredient)
    if title not in recipes :
        recipes.setdefault(title,[]).append(ingredient)
    else : recipes[title].append(ingredient)
    print (title , "ingredients :" , ingredients)
recipes[title].remove('end')
print ("Your Recipe Collection includes the following: ==> ", recipes)


#print (ingredients)
