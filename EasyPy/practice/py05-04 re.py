import re

isok = False
while isok == False:
    b = input('数を入れてね: ')
    if not re.match(r"^\d\d\d\d$",b):
        print('Type 4 digit')
    else: 
        isok = True
print(b[0])
print(b[1])
print(b[2])
print(b[3])



