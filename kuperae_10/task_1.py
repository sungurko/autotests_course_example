# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name(start):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    while start > 0:
        letter = ''.join([random.choice(letters) for _ in range(random.randint(1, 16))])
        letter1 = ''.join([random.choice(letters) for _ in range(random.randint(1, 16))])
        yield f'{letter} {letter1}'
        start -= 1


word = generate_random_name(4)
print(next(word))
print(next(word))
print(next(word))
print(next(word))
