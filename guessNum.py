import random

secretNum = random.randint(1,20)
print('Guess 1 to 20 NO.')

for i in range(6):
    print('Input No.')
    gs = int(input())

    if gs < secretNum:
        print('Your guess is Smaller')
    elif secretNum < gs:
        print('Your guess is Bigger')
    else: 
        break 

if gs == secretNum:
    print(('Right! in ')+ str(i) +
        ' times!!')
else:
    print('Sorry, the answer is: '
        + str(secretNum))