"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
first_sentenсes = input('Введитие первую строку: ').lower().strip()
second_sentenсes = input('Введитие вторую строку: ').lower().strip()


def main(first_sentenсes, second_sentenсes):
    if first_sentenсes.isdigit() or second_sentenсes.isdigit():
      return 0
    elif len(first_sentenсes) == len(second_sentenсes):
      return 1
    elif len(first_sentenсes) != len(second_sentenсes) and len(first_sentenсes) > len(second_sentenсes):
      return 2
    elif len(first_sentenсes) != len(second_sentenсes) and second_sentenсes == 'learn':
      return 3


if __name__ == "__main__":
    print(main(first_sentenсes, second_sentenсes))
