# Дано 2 строки a, b
a = 'инженер'
b = 'тестировщик'

# Найдем первые 2 символа строк a и b
first_a = a[:2]
first_b = b[:2]

# Поменяем местами найденные символы в строках a, b
# И объединим их в одну разделив пробелом
result = a.replace(first_a, first_b) + ' ' + b.replace(first_b, first_a)

# Выведем на печать результат
print('Результат:', result)
