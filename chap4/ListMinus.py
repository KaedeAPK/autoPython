spam = ['cat','bat','elephant']
print('[-1]: '+str(spam[-1]))
# List[-1] is the end val

print('The '+ spam[-1]+ 
' is afraid of the ' + spam[-3])

spam2 = ['cat','bat','rat','eleph']

# Not include end value[n:m-1]

# [0] to [3]
print(spam2[0:4])
# [1] to [2]
print(spam2[1:3])
# [0] to [3] 
print(spam2[0:-1])

print()
# [0] to [1]
print(spam2[:2])
# to Last
print(spam2[1:])
# all, same.
print(spam2[:])
print(spam2)

print(len(spam2))