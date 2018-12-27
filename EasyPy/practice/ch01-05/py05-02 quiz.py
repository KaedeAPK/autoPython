import random
a = random.randint(0,9)
print(a)

b = int(input('数を入れてね！ > '))
if a == b:
    print('当たり！すごいね！')
else:
    print('ざんねん... はずれ！')
