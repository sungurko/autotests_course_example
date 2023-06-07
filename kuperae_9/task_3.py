# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases


with open(r'.\test_file\task_3.txt', 'r', encoding='utf-8') as file:
    read_file = ' '.join([i.rstrip() for i in file.readlines()]).split('  ')
    three_most_expensive_purchases = sum(sorted([sum(map(int, (i.split(' ')))) for i in read_file])[-3:])


assert three_most_expensive_purchases == 202346
