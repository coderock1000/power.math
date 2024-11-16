def computepower(x, y):
    result = 1

    while(y > 0):

        if y % 2 == 0:
            x = x*x
            y >>= 1

        else:
            result = result * x
            y = - 1

    return result

x = int(input(' enter x of x^y : '))
y = int(input(' enter y of x^y : '))
print('total : ',computepower(x, y))