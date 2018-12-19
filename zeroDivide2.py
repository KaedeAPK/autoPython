def spam(dividePy):
    return 42/dividePy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error,不正な引数です')
    # What's the diff