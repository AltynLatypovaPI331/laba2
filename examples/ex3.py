'''
 Внутренние функции
'''
# Пример внутренней функции
def outer(o_p1, o_p2):
    def inner(i_p1, i_p2):
        return i_p1 + i_p2
    return inner(o_p1, o_p2)
print(outer(1,20))

# Пример без замыкания
def outer(out_param):
    def inner(in_param):
        return f'Outer def have value: {in_param}'
    return inner(out_param)
print(outer('TEST'))

# Пример с замыканием
def outer2(out_param):
    def inner2():
        return f'Outer def have value: {out_param}'
    return inner2
value = outer2('TEST')
print(value())

