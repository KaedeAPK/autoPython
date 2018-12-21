myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('My pets names are '+ str(myPets))
name = input('Type my pet name: ')
if name not in myPets:
    print(name + ' is not my pet name.')
else :
    print(name + ' is my pet!!')