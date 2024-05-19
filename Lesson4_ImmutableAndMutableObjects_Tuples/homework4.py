immutable_var = ('String', 2024, False)
print(immutable_var)
# immutable_var[0] = 'Other string' #TypeError: 'tuple' object does not support item assignment
# Кортеж нельзя изменить, так как кортежи содержат не сами объекты, а ссылки на объекты. Однако мы легко можем изменить
# вложенный изменяемый объект, например список
mutable_list = ['String', 2023, True]
print(mutable_list)
mutable_list[0] = 'Other string'
mutable_list[1] = 2024
mutable_list[2] = False
print(mutable_list)
