number = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
try:
    res = number / number_2
except ZeroDivisionError:
    res = 'Вы что? Пытаетесь делить на нуль!'
print(f'Результат: {res}')