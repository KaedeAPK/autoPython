
print('\nHit & Blowのプログラムです. 数値も場所も同じ場合はHitが加算され,\
数値はあっているけど違う場所で使われている場合はBlowを加算します。')

b = [1,2,3,0,] 
a = [0,1,2,3,]
    # b[0]= a[1], b[1]= a[2],b[3]= a[0] are True.

# hit:  0
# blow: 1
print()

for f in range(4): # as b?
        for i in range(4): # as a?
            print('f: ', str(f),'-----------------------')
            print(' ','i: ', str(i),'-------------------\n')

            print( 'b[', f, ']',b[f] ,'!=', 'a[', f, ']', a[f],'and: ',(b[f] != a[f]))
            print( 'b[', i, ']',b[i] ,'!=', 'a[', i, ']', a[i],'and: ',(b[i] != a[i]))
            print( 'b[', f, ']',b[f] ,'==', 'a[', i, ']', a[i],': ',(b[f] == a[i]))
            print('  ',
                (b[f] != a[f])and\
                (b[f] == a[i])and\
                (b[i] != a[i]),
            '\n')

# [f]同列のhitを取り除いて
# [i]同列のhitを取り除く、0から3まで各自繰り返して比較Lう？！＠＠＠

# b[0]と            a[0,1,2,3]
#   a[0]を比較       b[0,1,2,3]
#       
#   a[1]を比較
#       b[0]!= a[0], 0同士,縦が被ってないか
#       b[1]!= a[1], 1同士被ってないか
#       b[0] = a[1]
#   a[2]を比較
#       b[0]!= a[0], 0同士被ってないか
#       b[2]!= a[2], 2同士被ってないか
#       b[0] = a[2]
#   a[3]を比較

# b[1]とa[0-3]を比較
# b[2]とa[0-3]を比較
#   a[1]を比較 ,i[1]
#       b[2]!= a[2], 2同士,縦が被ってないか
#       b[1]!= a[1], 1同士被ってないか
#       b[2] = a[1]
# b[3]とa[0-3]を比較




# b[f] != a[f]
# b[f] == a[i]
# b[i] != a[i]

