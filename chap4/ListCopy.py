
import copy
spam = ['a','b','c','d',]
cheese = copy.copy(spam)
cheese[1] = 42
print(spam, '\n', cheese)

intb = [1,2,3,4,5,]
things = [spam,intb]

print(things)

cThings = copy.copy(things)
print(cThings)

