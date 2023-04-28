summing = lambda num_1, num_2: num_1 + num_2
subtraction = lambda num_1, num_2: num_1 - num_2
multiplication = lambda num_1, num_2: num_1 * num_2
division = lambda num_1, num_2: num_1 / num_2


def main():
    result = 0
    sign = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if sign in ['+', '-', '*', '/']:
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите второе число: '))
        if isinstance(num_1, (int, float)) and isinstance(num_2, (int, float)):
            if sign == '+':
                result = summing(num_1, num_2)
            elif sign == '-':
                result = subtraction(num_1, num_2)
            elif sign == '*':
                result = multiplication(num_1, num_2)
            elif sign == '/':
                try:
                    result = division(num_1, num_2)
                except ZeroDivisionError:
                    print('На нуль делить нельзя!')
                    main()
        else:
            print('Неверное число')
            main()
    elif sign == '0':
        exit()
    else:
        print('Неверный ввод. Попробуйте снова.')
        main()
    print(result)
    main()


main()
