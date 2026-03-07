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

def main():
    
    goods = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    sale = 0
   
  # суммарное количество продаж для каждого товара
    def total_phones_sold(phones_sold):
      total_sold = 0
      for sold in phones_sold:
        total_sold += sold
        return total_sold
    
    for one_goods in goods:
      phones_sold = total_phones_sold(one_goods['items_sold'])
      print(f'суммарное количество продаж {one_goods["product"]}: {phones_sold}')
  # конец подсчета суммарного количества продаж для каждого товара
    
  # среднее количество продаж для каждого товара
    def avg_total_phones_sold(phones_sold):
      total_sold = 0
      for sold in phones_sold:
        total_sold += sold
        return total_sold / len(phones_sold)
    
    for one_goods in goods:
      phones_sold = round(avg_total_phones_sold(one_goods['items_sold']), 2)
      print(f'Среднее количество продаж {one_goods["product"]}: {phones_sold}')
  # конец подсчета среднего количества продаж для каждого товара
  
  # суммарное количество продаж всех товаров
  
    
if __name__ == "__main__":
    main()
