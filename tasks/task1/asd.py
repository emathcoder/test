from math import sqrt
from fractions import Fraction

# 3x^2 - 14x - 5 = 0
b = -14
a = 3
c = -5

d = b ** 2 - 4 * a * c
new_d = sqrt(d)

x1 = (-b + new_d) / (2 * a)

tmp1 = -b - new_d
tmp2 = -b + new_d

x2 = Fraction(tmp1, tmp2)
print(x1, x2)

answer1 = 3 * x1 ** 2 - 14 * x1 - 5
answer2 = 3 * x2 ** 2 - 14 * x2 - 5

print(answer1, answer2)

