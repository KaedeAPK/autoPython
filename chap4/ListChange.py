spam = ['cat','bat','rat',
    'elephant']
spam[1] = 'aardvark'
print(spam)

spam[2] = spam[1]
print(spam)

spam[-1] = 123
print(spam)

spam += ['a','b','c']
print(spam)