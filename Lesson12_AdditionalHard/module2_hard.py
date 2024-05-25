import sys


def get_password(val):
    password = ''
    for i in range(1, val):
        for j in range(i + 1, val):
            if val % (i + j) == 0:
                password += str(i)
                password += str(j)

    return password


while True:
    value = input('Введите число о 3 до 20: ')
    if value.isdigit() and 3 <= int(value) <= 20:
        print('Ваш пароль:', get_password(int(value)))
    else:
        print('Некорректный ввод:', value)
        continue
    print('Хотите продолжить подбор пароля д/н? ')
    while True:
        continue_ = input()
        if continue_ == 'д':
            break
        elif continue_ == 'н':
            sys.exit(0)
