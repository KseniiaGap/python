# Способ решения с помощью функции sort
def my_func(f_n, s_n, th_n):
    list_1 = [f_n, s_n, th_n]
    list_1.sort(reverse=True)
    summa = list_1[0] + list_1[1]
    print(summa)


first_number = 10
second_number = 45
third_number = 87
my_func(first_number, second_number, third_number)


# Способ решения без функции sort
def func(f_n, s_n, th_n):
    list_1 = [f_n, s_n, th_n]
    print(list_1)
    maximum = 0
    sec_maximum = 1
    for i in range(len(list_1)):
        if list_1[i] > list_1[i - 1]:
            sec_maximum = maximum
            maximum = list_1[i]
    summa = sec_maximum + maximum
    print(summa)


first_number = 10
second_number = 45
third_number = 87
func(first_number, second_number, third_number)
