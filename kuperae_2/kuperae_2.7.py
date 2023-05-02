# Дана 2 строки из неповторяющихся символов
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'

# Найдем индексы первого вхождения символа первой строки во вторую
w = second_string.find(first_string[0])
t = second_string.find(first_string[1])
f = second_string.find(first_string[2])

# Найдем минимальный и максимальный индекс
start = min(w, t, f)
stop = max(w, t, f)

# Сделаем срез по минимальному и максимальному индексу
result = second_string[start:stop + 1]

# Выведем на печать результат
print('Срез минимальной длины:', result)
