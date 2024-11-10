from datetime import date, datetime
# Функция для расчета возраста пользователя
def cal_age(bdate_str):
  try:
    bdate = datetime.strptime(bdate_str, '%d.%m.%Y').date()
  except ValueError:
    print("Неверный формат даты рождения. Пожалуйста, введите дату в формате день.месяц.год")
    return None

  today = date.today()
  age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
  return age

# Получение даты рождения пользователя
bdate_str = input("Введите свою дату рождения в формате  день.месяц.год: (пример: 25.8.2004): ")

# Вычисление и вывод возраста
age = cal_age(bdate_str)
if age is not None:
  print(f"Ваш возраст: {age} лет")
