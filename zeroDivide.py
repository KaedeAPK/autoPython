# P.73
def spam(dividePy):
    try:
        return 42/dividePy
    except ZeroDivisionError:
        print('Error, incorrect val.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
