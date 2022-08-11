# simpson.py
# シンプソンの公式
# f(x) = exp(x)
# 区間[a, b]
# a = 0, b = 1

import random
import math

def f(x):
    return math.exp(x)

n = 1000
hx = 1.0 / float(n)
sum = f(0)
x = hx
for i in range(1, int(n/2)):
    sum += f(x) * 4.0 + f(x + hx) * 2.0
    x += hx * 2.0
sum += f(x) * 4.0 + f(1.0)
est = sum * hx / 3.0
print(est)