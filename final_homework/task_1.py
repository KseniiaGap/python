#Каждое из слов «разработка», «сокет», «декоратор» представить в буквенном
#формате и проверить тип и содержание соответствующих переменных.
#Затем с помощью онлайн-конвертера преобразовать в набор кодовых точек Unicode
#(НО НЕ В БАЙТЫ!!!) и также проверить тип и содержимое переменных.

f_word = 'разработка'
sec_word = 'сокет'
th_word = 'декоратор'
f_letter = list(f_word)
print(f_letter)
sec_letter = list(sec_word)
print(sec_letter)
th_letter = list(th_word)
print(th_letter)
for line in f_letter:
    print('Тип переменной: {}\n'.format(type(line)))
    print('Содержание переменной - {}\n'.format(line))
for line in sec_letter:
    print('Тип переменной: {}\n'.format(type(line)))
    print('Содержание переменной - {}\n'.format(line))
for line in th_letter:
    print('Тип переменной: {}\n'.format(type(line)))
    print('Содержание переменной - {}\n'.format(line))

f_word=u'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
sec_word=u'\u0441\u043e\u043a\u0435\u0442'
th_word=u'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(f_word),type(sec_word),type(th_word))
print(f_word, sec_word, th_word)




