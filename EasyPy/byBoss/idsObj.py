import copy

print('1rst, 3:', id(3))
a = 3
print('id(a):',id(a))
print('id(3):',id(3))

b = a
print('id(b):',id(b),'\n')

b = 4
print('id(b)',id(b))
print('id(4)',id(4),'\n')

b = 5
print('id(b)',id(b))

print('id(3)',id(3),'\n')

l = [1,2,3]
print(l, id(l))
c = l
print(c, id(c))
c = copy.copy(l)
print(c, id(c))

