cat = input('type a name: ')
newCat =''

for index in range(len(cat)):
    newCat += cat[len(cat)-1-index]

print(newCat)