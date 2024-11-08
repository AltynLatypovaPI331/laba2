'''
Аргументы и параметры функции
'''
# Пример функции с одним аргументом
def example(color):
    if color == "green":
        return "This is tree"
    elif color == "blue":
        return "This is sky"
    else:
        return "I don't know"
what_is_it = example('red')
print(what_is_it)

# Пример со значением None
example = 0
if example is None:
    print("It's nothing")
else:
    print("It's something")

# Пример позиционных аргументов
def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}
my_cat = cat('Pes', 'Ginger', 5)
print(my_cat)

# Пример аргумент – ключевые слова
def cat(name, color, age):
    return {'name': name, 'color': color, 'age': age}
my_cat = cat(color = 'Ginger', age = 5, name = 'Pes')
print(my_cat)

# Пример получения/разбиения аргументов – ключевых слов с помощью символа *
def example_args(*args):
    print('Positional argument tuple:', args)
example_args()
example_args(1, 2, 4, 5, 6, 7, 'argument')




