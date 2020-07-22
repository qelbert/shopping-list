import itertools

options = [
    ("Minced Meat Soup", {'minced meat', 'potatoes', 'frozen vegetable'}),
    ("Sunday Soup", {'chicken with bones', 'noodles', 'soup vegetable'}),
    ("Gulas", {'pork meat', 'food cream', 'potatoes', 'onion', 'frozen peas'}),
]

print ("What would you like to cook on weekend?")
print ("Here are the options:")
for option, (name, values) in enumerate(options, 1):
    print (str(option)+". "+ name)

choose = input("> ")

try:
    shopping_list = [options[int(choice.strip())-1][1] for choice in choose.split(",")]
    print ("Buy " + ", ".join(itertools.chain.from_iterable(shopping_list)) + ".")
except (IndexError, ValueError):
    print ("Hmmm. No such food on the list.")
