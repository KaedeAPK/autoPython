import random

a = [
    random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9),
    ]
while True:
# make input 4 digits
    # Flagをパタン！　　　　　　　　　　
    isOk = False
    while isOk == False:
        b = input('Type numbers! ')
        if len(b) != 4:
            print('Input 4 digits plz')
        else:
            # Flag input 4 digits
            numOk = True
            for i in range(4):
                # 0から9の範囲を超えていればprint()。
                # numOkをFalseに。そして中断。
                if (b[i] < '0') or ('9'< b[i]):
                    print(str(b[i])+ ' is Not a number.')
                    numOk = False
                    break
                # numberが数値ならば倒れてるFlagを立てる
                if numOk:
                    isOk = True
    hit = 0
    for i in range(4):
        if a[i] == int(b[i]):
            hit+=1
    
    # blow, very difficult
    blow = 0
    for i in range(4):
        for f in range(4):
            if (a[i] == int(b[f])) and (a[i] != int(b[i])) and (a[i] != int(b[f])):
                blow += 1
                break
    print('Hit: '+ str(hit))
    print('Blow: '+ str(blow))

# Write Down Flow Chart

