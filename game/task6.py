'''
Игра «камень-ножницы-бумага» в три раунда
'''
import random
def get_u():
 # Получение выбора пользователя
 while True:
  choice = input("Выберите камень, ножницы или бумага: ").lower()
  if choice in ["камень", "ножницы", "бумага"]:
   return choice
  else:
   print("Неверный выбор. Попробуйте еще раз.")
   
def get_c():
 # Cлучайный выбор компьютера
 choices = ["камень", "ножницы", "бумага"]
 return random.choice(choices)
def det(u_choice, c_choice):
 # Определение победителя
 if u_choice == c_choice:
  return "Ничья!"
 elif (u_choice == "камень" and c_choice == "ножницы") or \
    (u_choice == "ножницы" and c_choice == "бумага") or \
    (u_choice == "бумага" and c_choice == "камень"):
  return "Вы победили!"
 else:
  return "Компьютер победил!"

def play_game():
 # Запуск игры
 u_score = 0
 c_score = 0
 for round_n in range(1, 4):
  print(f"Раунд {round_n}:")
  u_choice = get_u()
  c_choice = get_c()
  print(f"Вы выбрали: {u_choice}")
  print(f"Компьютер выбрал: {c_choice}")
  result = det(u_choice, c_choice)
  print(result)
  if "Вы победили!" in result:
   u_score += 1
  elif "Компьютер победил!" in result:
   c_score += 1
 print("\n--- Итоги игры ---")
 print(f"Ваш счет: {u_score}")
 print(f"Счет компьютера: {c_score}")
 if u_score > c_score:
  print("Вы выиграли игру!")
 elif u_score < c_score:
  print("Компьютер выиграл!")
 else:
  print("Ничья!")
  
if __name__ == "__main__":
 play_game()




