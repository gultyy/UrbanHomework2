# 1. Сложная сдача
weight = 4.5  # кг
price = 34   # рубля за кг
cost = weight * price
print('Стоимость ' + str(weight) + ' кг (34 руб/кг) черешни: ' + str(cost))
while True:
    print('Введите количество денежных средств у покупателя:')
    money = int(input())
    if money >= cost:
        print('Сдача покупателя: ' + str(money - cost) + '\nСпасибо за покупку!',)
        break
    else:
        print('Недостаточно средств.')

