# 2112621-simE2-1.py
# 区間[a, b], [0, h]
# a = 0, b = 1
# 当たり外れ法、標本平均法、台形公式、シンプソンの公式

import random
import math

def f(x, y, z, R):
    return (math.sqrt(x**2 + y**2) - R)**2 + z**2


def atarihazure_normal(loop_N=10000000):
    n = 0
    L_R = 6
    s_r = 2

    for i in range(loop_N):
        x = (L_R + s_r) * random.random()
        y = (L_R + s_r) * random.random()
        z = s_r * random.random()
        if f(x, y, z, L_R) <= 4:
            n += 1
    est =  8 * (L_R + s_r)*(L_R + s_r)*s_r * float(n) / loop_N
    print('当たり外れ法終了')
    return est

def atarihazure_assignment(loop_N=10000000):
    n = 0
    L_R = 6
    s_r = 2

    for i in range(loop_N):
        x = (L_R + s_r) * random.random()
        y = (L_R + s_r) * random.random()
        z = s_r * random.random()
        if f(x, y, z, L_R) <= 4:
            if x*x + (y - 6)*(y - 6) < 1:
                continue
            n += 1
    est =  8 * (L_R + s_r)*(L_R + s_r)*s_r * float(n) / loop_N
    print('当たり外れ法終了')
    return est

def main():
    out_1 = atarihazure_normal()
    out_2 = atarihazure_assignment()

    print(out_1)
    print(out_2)

if __name__ == '__main__':
    main()
    