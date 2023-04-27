# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить обратное
# преобразование (используя методы encode и decode)

list_1 = ['разработка', 'администрирование', 'protocol', 'standard']
for i in list_1:
    a = i.encode(encoding='utf-8')
    print(a, type(a))
    b = bytes.decode(a, encoding='utf-8')
    print(b, type(b))
