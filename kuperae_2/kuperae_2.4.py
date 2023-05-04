# Дан абсолютный путь до файла
a = r'C:\Program Files\Common Files\microsoft shared\EQUATION\EQNEDT32.EXE'
# Найдем название диска, корневой папки и файла без расширения
file_name = a.split('\\')[-1][:-3]
disc_name = a.split('\\')[0].rstrip(':')
folder_name = a.split('\\')[1]

# Выведем на печать результаты
print('Название файла:', file_name,
      '\nНазвание диска:', disc_name,
      '\nКорневая папка:', folder_name)
