# Дано квадратное уравнение a * x2 ** 2 + b * x2 + c = 0
a = 6
b = 9
c = 2

discriminant = b ** 2 - 4 * a * c
x1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
x2 = round((-b - discriminant ** 0.5) / (2 * a), 2)

print('Дискриминант равен', discriminant,
      '\nПервый корень равен:', x1,
      '\nВторой корень равен:', x2,
      )
