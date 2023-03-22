# Способ решения с помощью функции sort

list_1 = [1, 3, 8, 0, 23, 1]
list_1.sort(reverse=True)
print(list_1)
sum = list_1[0] + list_1[1]
print(sum)



# Способ решения без функции sort

list_1 = [1, 3, 8, 0, 23, 1]
maximum = 0
sec_maximum = 1
for i in range(len(list_1)):
   if list_1[i] > list_1[i - 1]:
       sec_maximum = maximum
       maximum = list_1[i]
sum = sec_maximum + maximum
print(sum)
