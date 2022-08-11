# atarihazure.py
# 当たり外れ法
# f(x) = exp(x)
# 区間[a, b], [0, h]
# a = 0, b = 1

import random
import math

loop_N = 10000000
n = 0
a = 0
b = 1
h = 3

for i in range(loop_N):
    x = a + (b - a) * random.random()
    y = h * random.random()
    if y < math.exp(x):
        n += 1
est = (b - a) * h * float(n) / loop_N
print(est)