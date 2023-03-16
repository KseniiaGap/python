revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    print(f'Финансовый результат - прибыль. Ее величина: {costs}')
    return_on_revenue = (revenue - costs) / revenue
    print(f'Рентабельность выручки = {return_on_revenue}')
    employee = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника = '
          f'{(revenue - costs) / employee}')
elif revenue == costs:
    print('Вы ничего не заработали и ничего не потеряли.')
else:
    print(f'Финансовый результат - убыток. Его величина: {costs - revenue}')
