# Дан абсолютный путь до файла
a = 'C:\\Users\\kuperae\Desktop\pythonProject_course\kuperae_2\kuperae_2.4.py'

# Найдем название диска, корневой папки и файла без расширения
file_name = a.split('\\')[-1][:-3]
disc_name = a[0]
folder_name = a.split('\\')[1]

# Выведем на печать результаты
print('Название файла:', file_name,
      '\nНазвание диска:', disc_name,
      '\nКорневая папка:', folder_name)
