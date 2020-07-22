import itertools
import json

#Open json dictionary to (r)ead through
with open('recipes.json', 'r') as fp:
    recipes = json.load(fp)

print("\n\n Welcome! Here are your options: \n\n")

options = list()

#Add or Update a Recipe in json dictionary
class groceryList():
    def viewRecipeCollection():
            x = sorted(recipes.items(), key=lambda x: x[0])
            for recipe , (name, values) in enumerate(x, 1):
                print(str(recipe) + ". "+ str(name)+ " : " + str(values) +"\n")
    def addOrUpdateRecipe():
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
                #or skip if ingredient is already in list
            if ingredient in recipes[title] :
                print ("that ingredient is already in your list")
                continue
            #otherwise append additional ingredent to list of values
            else : recipes[title].append(ingredient)
            print (title , "ingredients :" , recipes[title])

        #Open json dictionary to (w)rite -- actually ReWrite -- the entire updated dictionary onto
        with open('recipes.json', 'w') as fp:
            json.dump(recipes, fp)
        print ("Your Recipe Collection includes the following: ==> \n\n")

        #Create a sorted list of tuples from the recipe dictionary; enumerate and print each tuple
        #https://pybit.es/dict-ordering.html
        groceryList.viewRecipeCollection()

    def deleteRecipe():
        print("Here is your current list\n\n")
        groceryList.viewRecipeCollection()
        delete = input('What recipe would you like to delete from your collection?')
        del recipes[delete]
        with open('recipes.json', 'w') as fp:
            json.dump(recipes, fp)
        print("\n\nHere is your updated list: \n\n")
        groceryList.viewRecipeCollection()

#remove the '_' items from the class' directory list
for funct in dir(groceryList()):
    if "_" in funct : continue
    options.append(funct)

#enumerate the functions in the class' directory and prints as a list
for counter, value in enumerate(options, 1):
    print(str(counter) +". "+ value)

#user selects function
selection = input("\n\n what would you like to do?")
count = 0
for choice in options:
    count = count + 1
    if count != int(selection) : continue
    else:
        print("\n\nYou've chosen to "+ str(choice) + "!\n\n")
        print(getattr(groceryList, choice)())
