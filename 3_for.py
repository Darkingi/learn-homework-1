"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
all_phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]
# суммарное количество продаж для каждого товара
def main():
    def phone_sold_info():
        items_sold = 0
        for phone in all_phones:
            value_sold = 0
            for one_sell in phone['items_sold']:
                value_sold += one_sell
            items_sold += value_sold
            print(f'суммарное количество продаж {phone['product']}: {items_sold}')
    print(phone_sold_info())
    print('__________________') #Наглядный отступ
    
    def avg_phones_sold_info():
        avg_sold = phone_sold_info
        for avg_sold_one_phone in all_phones:
            produc_phone = 0
            for one_avg_item in avg_sold_one_phone['product']:
                produc_phone += one_avg_item
            avg_sold / len(avg_sold_one_phone)
            print(f'суммарное количество продаж {avg_sold_one_phone['product']}: {avg_sold}')
    print(avg_phones_sold_info())
if __name__ == "__main__":
    main()

'''
Правильно ли я понимаю, что нам надо создать первую функцию, которая будет считать  суммарное количество продаж для каждого товара,
А потом сделать вторую функцию, которая из первой функции будет брать данные и считать среднее количество продаж для каждого товара?
'''



'''
def total_phone_sold():
        total_sold = 0
        for sold in all_phones:
            one_phone = 0
            for number in sold['items_sold']:
                one_phone += number
            total_sold += one_phone
            return total_phone_sold


    for one_goods in all_phones:
        phones_sold = total_phone_sold()
        print(f'суммарное количество продаж {one_goods["product"]}: {phones_sold}')
# конец подсчета суммарного количества продаж для каждого товара
    print('') # отступ для удобного просмотра
# среднее количество продаж для каждого товара
    def avg_phones_sold():
        total_sold = total_phone_sold
        for sold in phones_sold:
            total_sold += sold
        return total_sold / len(phones_sold)
    
    for one_goods in all_phones:
        phones_sold = avg_phones_sold()
        print(f'Среднее количество продаж {one_goods["product"]}: {phones_sold}')
# конец подсчета среднего количества продаж для каждого товара
    print('') # отступ для удобного просмотра
# суммарное количество продаж всех товаров
    total_phones_sold = 0
    
    """
суммарное количество продаж iPhone 12: 4243
суммарное количество продаж Xiaomi Mi11: 4092
суммарное количество продаж Samsung Galaxy 21: 4094

сумарное количество продаж всех товаров: 12282

Должно быть 12429 т.к. 4243 + 4092 + 4094 = 12429
    """
    for phones_sold in all_phones:
        total_phones_sold += total_phone_sold()
    print(f'Суммарное количество продаж всех товаров: {total_phones_sold}')
# конец подсчета суммарного количество продаж всех товаров
    print('') # отступ для удобного просмотра   
    
# среднее количество продаж всех товаров
    avg_phones_sold = 0
    for one_avg_phones_sold in all_phones:
        avg_phones_sold += total_phone_sold()
    avg_phones_sold = int(avg_phones_sold / len(all_phones))
    print(f'Среднее количество продаж всех товаров: {avg_phones_sold}')
# конец подсчета среднего количества продаж всех товаров
    print('') # отступ для удобного просмотра
'''