# daikei.py
# 台形公式
# f(x) = exp(x)
# 区間[a, b]
# a = 0, b = 1

import random
import math

def f(x):
    return math.exp(x)

n = 1000
h = 1.0 / float(n)
sum = f(0) / 2.0

for i in range(1, n):
    x = float(i) * h
    sum += f(x)

sum += f(1.0) / 2.0
est = sum * h
print(est)