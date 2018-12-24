
b = [0,2,4,5,] 
a = [0,1,2,3,]

# hit:  0
# blow: 1
print()

for f in range(4):
        for i in range(4):
            print('f: ', str(f), 'i: ', str(i),'-------------------\n')

            print( 'b[', f, ']',b[f] ,'!=', 'a[', f, ']', a[f],'and',)
            print( 'b[', f, ']',b[f] ,'==', 'a[', i, ']', a[i],'and',)
            print( 'b[', i, ']',b[i] ,'!=', 'a[', i, ']', a[i],'\n')

            



# b[f] != a[f]
# b[f] == a[i]
# b[i] != a[i]


# a[i] == b[f]
# a[i] != b[i]
# a[f] != b[f]