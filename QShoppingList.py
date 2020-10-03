#completed 12:24am Sept 12, 2018
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
            ingredient = input("please type in new ingredients one by one. When done, type 'end'.")
            if ingredient == "end" :
                break
            #removing ingredients from an existing recipe
            elif ingredient == "remove":
                try:
                    print(title, ": ", recipes[title])
                except:
                    print("that recipe is not found, please try again.")
                    break
                ringredient = input("what ingredient would you like to remove from the " + title + " recipe?")
                try:
                    recipes[title].remove(ringredient)
                except:
                    print("that ingredient is not found in " + title + " please select from the ingredients below.")
                    print(title, ": ", recipes[title])
                    continue
            #adding ingredients to existing or new recipes
            elif title not in recipes :
                #within the 'recipes' .js file/dictionary create a key that sets an empty list as its value. Append first ingredient to list.
                recipes.setdefault(title,[]).append(ingredient)
                #or skip if ingredient is already in list
            elif ingredient in recipes[title] :
                print ("that ingredient is already in your list")
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

    def makeGroceryList():
        groceryList.viewRecipeCollection()
        x = sorted(recipes.items(), key=lambda x: x[0])
        shoppingList = []
        while True:
            selectionr = input("\n\n Select each recipe to add to your list, one by one. When done, type 'end'." )
            if selectionr == "end" : break
            else :
                countr = 0
                for choice in x:
                    countr = countr + 1
                    if countr != int(selectionr) : continue
                    else:
                        for ing in choice[1]:
                            if ing in shoppingList : continue
                            else :
                                shoppingList.append(ing)
        with open('slist.json', 'w') as fp:
            json.dump(shoppingList, fp)
        shoppingList.sort()
        print("Here's your shopping list! \n\n")
        print(shoppingList)
        ##edit = input("Would you like to remove any items from your list (Y or N)?")
        ##While True:
        ##    if edit == N : break
        ##    elif edit == Y :
        ##    pantry = input("Please type the ingredient you'd like to remove, one by one. When done, type 'end'.")

    def sortListByFavStore():
        with open('stores.json', 'r') as fp:
            stores = json.load(fp)

        with open('slist.json', 'r') as fp:
            slist = json.load(fp)
        storelist = []
        #create a list of all the store names that are located at the primary location
        for ing2 in slist:
            y = stores[ing2][0]
            for k, v in y.items():
                if k in storelist : continue
                storelist.append(k)

        for storenames in storelist :
            thisstore = []
            #iterates through ingredients in shopping list and groups them according to their primary store name
            for ing2 in slist:
                y = stores[ing2][0]
                for k, v in y.items():
                    if k == storenames :
                        thisstore.append(ing2)
            print(storenames)
            print(str(thisstore) + "\n\n")

#remove the '_' items from the class' directory list
for funct in dir(groceryList()):
    if "_" in funct : continue
    options.append(funct)

#enumerate the functions in the class' directory and prints as a list
for counter, value in enumerate(options, 1):
    print(str(counter) +". "+ value)

#user selects function
selection = input("\n\n what would you like to do?")
counto = 0
for choice in options:
    counto = counto + 1
    if counto != int(selection) : continue
    else:
        print("\n\nYou've chosen to "+ str(choice) + "!\n\n")
        print(getattr(groceryList, choice)())
