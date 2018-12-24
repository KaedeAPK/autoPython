
b = [1,2,3,0,] 
a = [0,1,2,3,]

# hit:  0
# blow: 1
print()

for f in range(4): # as b?
        for i in range(4): # as a?
            print('f: ', str(f),'-----------------------')
            print(' ','i: ', str(i),'-------------------\n')

            print( 'b[', f, ']',b[f] ,'!=', 'a[', f, ']', a[f],'and',)
            print( 'b[', f, ']',b[f] ,'==', 'a[', i, ']', a[i],'and',)
            print( 'b[', i, ']',b[i] ,'!=', 'a[', i, ']', a[i])
            print(
                (b[f] != a[f])and\
                (b[f] == a[i])and\
                (b[i] != a[i]),
            '\n')

# [f]同列のhitを取り除いて
# [i]同列のhitを取り除く、0から3まで各自繰り返して比較Lう？！＠＠＠


# b[f] != a[f]
# b[f] == a[i]
# b[i] != a[i]


# a[i] == b[f]
# a[i] != b[i]
# a[f] != b[f]