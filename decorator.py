def is_prime(func):
    def wrapper(a, b, c):
        sum = func(a, b, c)
        if sum % 2 != 0:
            print('Простое')
        else:
            print('Составное')
        return sum
    return wrapper
@is_prime
def sum_three(a, b, c):
    res = a + b + c
    return res

#sum_three = is_prime(sum_three)
a = sum_three(2, 3, 6)
print(a)
