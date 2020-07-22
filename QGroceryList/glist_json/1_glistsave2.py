import itertools
import json

#Open json dictionary to (r)ead through
with open('recipes.json', 'r') as fp:
    recipes = json.load(fp)

options = input("what would you like to do?")

#Add or Update a Recipe in json dictionary
def updateRecipe():
    title = input("What is the name of your recipe?")
    ingredient = None
    while True :
        print("type 'remove' to delete existing ingredients--OR")
        ingredient = input("please type in ingredients one by one. When done, type 'end'.")
        if ingredient == "end" :
            break
        #removing ingredients from an existing recipe
        if ingredient == "remove":
            try:
                print(title, ": ", recipes[title])
            except:
                print("that recipe is not found, please try again.")
                break
            ringredient = input("what ingredient would you like to remove from the " + title + " recipe?")
            recipes[title].remove(ringredient)
            continue
        #adding ingredients to existing or new recipes
        if title not in recipes :
            #within the 'recipes' .js file/dictionary create a key that sets an empty list as its value. Append first ingredient to list.
            recipes.setdefault(title,[]).append(ingredient)
            continue
        if ingredient in recipes[title] :
            #or skip if ingredient is already in list
            print ("that ingredient is already in your list")
            continue
        else : recipes[title].append(ingredient)
            #otherwise append additional ingredent to list of values
        print (title , "ingredients :" , recipes[title])

    #Open json dictionary to (w)rite -- actually ReWrite -- the entire updated dictionary onto
    with open('recipes.json', 'w') as fp:
        json.dump(recipes, fp)
    print ("Your Recipe Collection includes the following: ==> \n\n")

    #Create a sorted list of tuples from the recipe dictionary; enumerate and print each tuple
    #https://pybit.es/dict-ordering.html
    x = sorted(recipes.items(), key=lambda x: x[0])
    for recipe , (name, values) in enumerate(x, 1):
        print(str(recipe) + ". "+ str(name)+ " : " + str(values) +"\n")

while True:
    if options == "update" :
        updateRecipe()
    else:
        print("you are SOL...there are no more options, SUCKA!!")
        break
