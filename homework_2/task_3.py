def func(name, date_of_birth, city_of_residence, mail, phone_number):
    print(f'{name} {date_of_birth} года рождения, проживает в городе '
          f'{city_of_residence}, email: {mail}, телефон: {phone_number}')
name = input('Введите ваше имя и фамилию: ')
date_of_birth = int(input('Введите ваш год рождения: '))
city_of_residence = input('Введите ваш город проживания: ')
mail = input('Введите ваш email: ')
phone_number = input('Введите ваш телефон: ')
func(name=name, date_of_birth=date_of_birth,
     city_of_residence=city_of_residence, mail=mail,
     phone_number=phone_number)