'''
Функции генераторы
'''
def my_generate(start=1, stop=10, step=2):
    number = start
    while number <= stop:
        yield number
        number += start
ranger = my_generate(1,9)

for value in ranger:
    print(value)
