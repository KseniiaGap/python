# Каждое из слов «class», «function», «method» записать в байтовом формате без
# преобразования в последовательность кодов не используя!!! методы encode и
# decode и определить тип, содержимое и длину соответствующих переменных.

var = [b'class', b'function', b'method']
for line in var:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержимое переменой: {}\n'.format(line))
    print('длина строки: {}\n'.format(len(line)))

