import random
# 5 times
print('random int')
for i in range(5):
    # 1 to 10 random int value
    print(random.randint(1,10))

import sys
while True:
    print('Type exit when you end')
    res = input()
    if res == 'exit':
        sys.exit()
    print(res + ': typed')