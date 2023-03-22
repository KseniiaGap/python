# Решение через dict

month = int(input("Введите число месяца: "))
dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето",
        7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень",
        12: "Зима"}
if dict.get(month):
    print(dict.get(month))
else:
    print("Такого месяца нет")



# Решение через list

month = int(input("Введите число месяца: "))
months = ['Зима','Весна','Лето','Осень',]
if month in [12, 1, 2]:
    print(months[0])
elif month in [3, 4, 5]:
    print(months[1])
elif month in [5, 7, 8]:
    print(months[2])
elif month in [9, 10, 11]:
    print(months[3])
else:
    print('Такого месяца нет')
