# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
count = 0
a1 = a
while a1 > b:
    a1 = a1 - b
    count += 1
print('Целочисленное деление', a, 'на', b, 'дает', count)
