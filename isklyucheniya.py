def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return 'Ошибка: невозможно преобразовать {} в целое число.'.format(s)

print(string_to_int("a"))

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'Ошибка: файл {} не найден.'.format(filename)
    except IOError:
        return 'Ошибка ввода/вывода при работе с файлом {}.'.format(filename)

print(read_file('pushkin.txt'))
print(read_file(5))

def divide_numbes(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Ошибка: деление на ноль.'
    except TypeError:
        return 'Ошибка: аргументы должны быть числами.'

print(divide_numbes(5, 0))
print(divide_numbes('a', 5))

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f'Ошибка: индекс {index} вне диапазона списка.'
    except TypeError:
        return 'Ошибка: индекс должен быть целым числом.'

my_list = ['Tural', 'Raul', 'Radmir']
print(access_list_element(my_list, 4 ))
print(access_list_element(my_list, 'x' ))