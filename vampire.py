# auto python p.34
print('君はだれ？')
name = input()
print('何歳？')
age = input()
age = int(age)
if name == 'Alice':
    print('やぁ、Alice')
elif age < 12:
    print('Aliceじゃないね、お嬢ちゃん。')
elif 2000 < age:
    print('Aliceはお前のような不死身ではない、吸血鬼め。')
elif 100 < age:
    print('Aliceじゃないね、お婆ちゃん。')
