def math_func(operation):
    if operation == 'div':
        def div(x, y):
            return x / y
        return div

    elif operation == 'multiply':
        def multiply(x, y):
            return x * y
        return multiply

print('Задача 1: Фабрика функций')
res_func = math_func('div')
print(res_func(5,2))
res_func2 = math_func('multiply')
print(res_func2(2,7))
try:
    print(res_func(2,0))
except:
    print('Error: Division by zero')


print('Задача 2: Лямбда-Функции')
squar = lambda x, y: x ** y
print(squar(3, 3)) # Выводит 6

def squar(x,y):
    return x ** y
print(squar(3,3))

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

res = Rect(2,4)
print(f'Стороны: {res.a}, {res.b}')
print('Площадь: {}'.format(res()))