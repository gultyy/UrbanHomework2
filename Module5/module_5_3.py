"""
Домашнее задание по уроку "Перегрузка операторов"

    Создайте новый проект в PyCharm
    Запустите созданный проект

Ваша задача:

    Создайте новый класс Building
    Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности
    self.numberOfFloors и строковый атрибут self.buildingType
    Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
    Полученный код напишите в ответ к домашему заданию
"""
class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building1 = Building(12, 'Многоэтажка')
building2 = Building(12, 'Многоэтажка')
print(building1 == building2)
building1 = Building(9, 'Многоэтажка')
building2 = Building(12, 'Многоэтажка')
print(building1 == building2)
building1 = Building(2, 'Частный дом')
building2 = Building(12, 'Многоэтажка')
print(building1 == building2)
