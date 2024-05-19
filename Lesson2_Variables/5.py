# 5. Автоматизируем простоту
while True:
    print('Введите натуральное число:')
    natural_number = input()
    if natural_number.isdigit() and int(natural_number) > 0:
        break

print('Введите любимое дело:')
favourite_business = input()
print((favourite_business + '\n') * int(natural_number))
