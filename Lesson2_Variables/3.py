#3. Самая простая задача на свете
while True:
    print('Введите натуральное число:')
    natural_number = input()
    if natural_number.isdigit() and int(natural_number) > 1:
        print(('Купи конструктор!\n') * int(natural_number))
        break