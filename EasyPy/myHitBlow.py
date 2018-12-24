
b = [1,2,3,0,] 
a = [0,1,2,3,]

# hit:  0
# blow: 4
for i in range(4):
    if (a[i]==b[i])\
    and ((b[i]==a[i+1]or a[i]==b[i+2]or a[i]==b[i+3])):
        print('True')
