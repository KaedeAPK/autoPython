import random

def getAns(ansNum):
    if ansNum == 1:
        return 'Really so.'
    elif ansNum == 2:
        return 'Without Question, so.'
    elif ansNum == 3:
        return 'Yes.'
    elif ansNum == 4:
        return 'So so,Plz do again.'
    elif ansNum == 5:
        return 'Ask me again later.'
    elif ansNum == 6:
        return 'Concentrate and Ask me again.'
    elif ansNum == 7:
        return 'My ans is No'
    elif ansNum == 8:
        return 'Outlook is not good.'
    elif ansNum == 9:
        return 'Very Suspective.'
    
# r = random.randint(1,9)
# fortune = getAns(r)
# print(fortune)
print(getAns(random.randint(1,9)))


    
    
    
    