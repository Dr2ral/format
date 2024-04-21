def sum_three(a, b, c):
    res = a + b + c
    return res
def is_prime(func):
    def wrapper(a, b, c):
        sum = func(a, b, c)
        if sum % 2 != 0:
            print('Простое')
        else:
            print('Составное')
        return sum
    return wrapper

result = is_prime(sum_three)
a = result(2, 3, 6)
print(a)
