def sum_three(x, y, z):
    res = x + y + z
    return res

def is_prime(x, y, z, func):
    fun = func(x, y, z)
    if fun % 2 != 0:
        print('Простое')
    else:
        print('Составное')
    print(fun)


result = is_prime(2, 4, 6,sum_three)