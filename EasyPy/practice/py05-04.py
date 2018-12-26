import random

isok = False

while isok == False:
    b = input('4ケタの数を入れてね! > ')
    if len(b) != 4:
        print('4ケタでおねがいします！')
    else:  
        k = True
        for i in range(4):
            if (b[i] < '0' or '9' < b[i]):
                    print(str(b[i])+'は数字ではありません')
                    k = False
                    break
        if k:
            isok = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])
