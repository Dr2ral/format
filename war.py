import warnings


def div_calculate(num1, num2):
        try:
           if num2 < 0.03:
             warnings.warn(f'делитель приближается к 0', UserWarning)
        except UserWarning as a:
            print(f'Предупреждение!: {a}')
        return num1 / num2

div_calculate(2, 0.01)

warnings.simplefilter('always', UserWarning)
div_calculate(2, 0.01)


warnings.simplefilter('ignore', UserWarning)
div_calculate(2, 0.01)


try:
    div_calculate(2, 0)

except:
    print('Ошибка: Введено число 0')

warnings.simplefilter('error', UserWarning)
div_calculate(2, 0.01)

