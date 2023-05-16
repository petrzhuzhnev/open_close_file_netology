# {'dish': [{'ingredient_name': 'ingredient', 'quantity': 'num', 'measure': 'sht' }]}
from pprint import pprint
with open('file.txt', 'rt') as file_read:
    cook_books = {}
    for line in file_read:
        dish = line.strip() #удаляет пробел табуляцию и перенос и берем первую строку так как file_read это <list>
        number_of_dishes = int(file_read.readline())
        ingredient = []
        for i in range(number_of_dishes): #'_' если значение не будет нигде использоваться
            # Берем третью строку с условием, что таких будет number_of_dishes
            ing = file_read.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ') #распаковка или множественно присваивание значений списка ing
            cook_book = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredient.append(cook_book)
            cook_books[dish] = ingredient
        file_read.readline()

    # pprint(cook_books, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = []
    for dish in dishes:
        if dish in cook_books:
            for ingr in cook_books[dish]:
                a = int(ingr['quantity']) * person_count
                ingr['quantity'] = a
                list_by_dishes.append(ingr)
    print(*list_by_dishes, sep = '\n')



get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2)
