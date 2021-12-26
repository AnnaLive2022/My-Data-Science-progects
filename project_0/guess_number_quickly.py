import numpy as np
from numpy import random
def game_v3(number: int = 1) -> int:
  """Сначала устанавливаем границы random числа, уменьшаем их в два раза, и находим random число,
     а потом изменяем границы поиска random числа  в зависимости от того, больше оно или меньше нужного.
     Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
  """
  attempt_counter = 0   # кол-во попыток
  prdict_number_min = 1  # нижняя граница поиска числа
  prdict_number_max = 101  # верхняя граница поиска числа
    
  while True:
    attempt_counter += 1
    predict_number = (prdict_number_max + prdict_number_min) // 2

    if number > predict_number:
       prdict_number_min = predict_number  # смещение нижней границы поиска числа
               
    elif number < predict_number:
      prdict_number_max = predict_number  # смещение верхней границы поиска числа
    
    else:
      break
  print(f'Количество попыток равно {attempt_counter}')
  return attempt_counter
game_v3(9)