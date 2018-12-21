catNames = []
while True:
    print('Type your cat'+str(len(catNames)+1) +"'s name." +
    'Press return key to end.')
    name = input()
    if name == '':
        break
    catNames += [name]
print('All:')
# nameが数になってる？？
for name in catNames:
    print('  ' + name)
