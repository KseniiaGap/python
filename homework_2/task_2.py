def func(num_1, num_2):
    try:
        res = num_1 / num_2
    except ZeroDivisionError:
        res = 'Вы что? Пытаетесь делить на нуль!'
    print(f'Результат: {res}')


number = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
func(number, number_2)
