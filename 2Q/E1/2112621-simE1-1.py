# 2112621-simE1-1.py
# f(x) = exp(x)
# 区間[a, b], [0, h]
# a = 0, b = 1
# 当たり外れ法、標本平均法、台形公式、シンプソンの公式

import random
import math


def f(x):
    return math.exp(x)


def atarihazure(loop_N=10000000):
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
    print('当たり外れ法終了')
    return est

def hyouhonheikin(loop_N = 10000000):
    a = 0
    b = 1
    sum = 0

    for i in range(loop_N):
        x = a + (b - a) * random.random()
        y = math.exp(x)
        sum += y
        
    mu = sum / float(loop_N)
    est = (b - a) * mu
    print('標本平均法終了')
    return est

def daikei(n=1000):
    h = 1.0 / float(n)
    sum = f(0) / 2.0

    for i in range(1, n):
        x = float(i) * h
        sum += f(x)

    sum += f(1.0) / 2.0
    est = sum * h
    print('台形公式終了')
    return est

def simpson(n=1000):
    hx = 1.0 / float(n)
    sum = f(0)
    x = hx
    for i in range(1, int(n/2)):
        sum += f(x) * 4.0 + f(x + hx) * 2.0
        x += hx * 2.0
    sum += f(x) * 4.0 + f(1.0)
    est = sum * hx / 3.0
    print('シンプソンの公式終了')
    return est

def relative_error(calc_v, true_v):
    return abs(calc_v - true_v) / true_v

def main():
    true_value = math.e - float(1)
    loop_N = 50000000
    n = 5000
    atarihazure_value = atarihazure(loop_N=loop_N)
    hyouhonheikin_value = hyouhonheikin(loop_N=loop_N)
    daikei_value = daikei(n=n)
    simpson_value = simpson(n=n)
    atarihazure_error = relative_error(atarihazure_value, true_value)
    hyouhonheikin_error = relative_error(hyouhonheikin_value, true_value)
    daikei_error = relative_error(daikei_value, true_value)
    simpson_error = relative_error(simpson_value, true_value)

    print('loop_N: ' + str(loop_N))
    print('n: ' + str(n))
    print('真値: '+ str(true_value))
    print('当たり外れ法 - 計算結果: ' + str(atarihazure_value))
    print('標本平均法 - 計算結果: ' + str(hyouhonheikin_value))
    print('台形公式 - 計算結果: ' + str(daikei_value))
    print('シンプソンの公式 - 計算結果: ' + str(simpson_value))
    print('')
    print('当たり外れ法 - 相対誤差: ' + str(atarihazure_error))
    print('標本平均法 - 相対誤差: ' + str(hyouhonheikin_error))
    print('台形公式 - 相対誤差: ' + str(daikei_error))
    print('シンプソンの公式 - 相対誤差: ' + str(simpson_error))
    print('')
    print('当たり外れ法, 標本平均法 - 誤差の比例値: ' + str(1/math.sqrt(loop_N)))
    print('台形公式 - 誤差の比例値: ' + str(n**(-2)))
    print('シンプソンの公式 - 誤差の比例値: ' + str(n**(-4)))



if __name__ == '__main__':
    main()