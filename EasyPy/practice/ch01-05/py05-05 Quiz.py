# coding: utf-8
import random

a = [
        random.randint(0,9),
        random.randint(0,9),
        random.randint(0,9),
        random.randint(0,9),
     ]
# a[] is ans, b[] is player's guess
#print( 'Ans: '+str(a[0])+ str(a[1])+ str(a[2])+ str(a[3]) )
print('Blow means in wrong position, but the number is included. ')

while True:
    # difine 4 dig or not
    isok = False
    while isok == False:
        # inside the intput() parents, appear to terminal?
        b = input('Input number: ')
        if len(b) != 4:
            print('Input 4 digits plz')
        else:
            numOk = True
            for i in range(4):
                if ( b[i]< '0') or ('9'<b[i]):
                    print(str(b[i])+ ' is Not a number.')
                    numOk = False
                    break
            if numOk:
                isok = True
    hit = 0
    for i in range(4):
        if a[i] == int(b[i]):
            hit +=1

    blow = 0
    for j in range(4):
        for i in range(4):
            if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j]!= int (b[j]) ):
                blow = blow + 1
                break
    print('Hit: '+ str(hit))
    print('Blow: '+ str(blow))

    if hit == 4:
        print('You won!!')
        break
                    
      
        



    
