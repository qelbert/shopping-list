x = list()
type(x)
print('This prints the entire directory for lists')
print(dir(x))
print("=============")
#y=dir(x)
#print(y)
#print("=============")
good = list()
print("=============")
print('This prints only the functions for lists')
for d in dir(x):
    if "_" in d: continue
    good.append(d)
print(good)
print("=============")
print('This prints the functions for lists, but numbered')
for counter, value in enumerate(good, 1):
    print(str(counter) +". "+ value)
