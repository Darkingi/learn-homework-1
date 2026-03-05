"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
  user_year = int(input('укажите ваш возраст: '))

  def check_year(user_year):
    if user_year == 0:
      return f'Ваш возраст: {user_year}, пора спать.'
    elif user_year > 0 and user_year <= 6:
      return f'Ваш возраст: {user_year}, пора в садик.'
    elif user_year > 6 and user_year <= 17:
      return f'Ваш возраст: {user_year}, пора в школу.'
    elif user_year > 18 and user_year <= 21:
      return f'Ваш возраст: {user_year}, пора в ВУЗ.'
    elif user_year > 22 and user_year <= 69:
      return f'Ваш возраст: {user_year}, пора на работу.'
    else:
      return 'Пора на бесконечную пенсию'

  user_can_go = check_year(user_year)
  print(user_can_go)

if __name__ == "__main__":
    main()