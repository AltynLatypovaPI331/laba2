"""
Функция, которая находит все числа, кратные заданной цифре X, в списке чисел.

"""
import random
def find_m(x, n):
 
 is_m = lambda num: num % x == 0
 m = list(filter(is_m, n))
 return m

# Генерация случайного списока чисел
n = [random.randint(0, 200) for _ in range(10)]

# Запрос цифры X от пользователя
while True:
 try:
  x = int(input("Введите X: "))
  if x == 0:
   print("Число не может быть равно 0. Попробуйте снова.")
  else:
   break
 except ValueError:
  print("Некорректный ввод. Введите целое число.")

# Поиск и вывод чисел, кратных X
m = find_m(x, n)
print(f"Сгенерированный список чисел {n}")
print(f"Числа, кратные {x}: {m}")
