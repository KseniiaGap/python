# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно
# записать в байтовом типе с помощью маркировки b'' (без encode decode).

# не смогла решить без encode

for line in ['attribute','класс','функция','type']:
    try:
        print(line,type(line),line.encode('ascii'), ' - encoding to bytes '
                                                    'successful ')
    except:
        print(line,type(line),' - not valid input for bytes string')