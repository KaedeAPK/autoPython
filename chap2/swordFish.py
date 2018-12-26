while True:
    print('あなたはだれ？')
    name = input()
    if name != 'Joe':
        continue
    print('こんにちはJoe,パスワードは何？🐟')
    passWord = input()
    if passWord == 'swordFish':
        break
print('認証しました。')