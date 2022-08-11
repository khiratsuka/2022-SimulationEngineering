# hyouhonheikin.py
# 標本平均法
# f(x) = exp(x)
# 区間[a, b]
# a = 0, b = 1

import random
import math

loop_N = 10000000
a = 0
b = 1
sum = 0

for i in range(loop_N):
    x = a + (b - a) * random.random()
    y = math.exp(x)
    sum += y
    
mu = sum / float(loop_N)
est = (b - a) * mu
print(est)