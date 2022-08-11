# 2112621-simE2-2.py
# 変数は適宜変更すること。

import random
import math
import numpy as np
from tqdm import tqdm
import csv

def create_pdf(mean):
    p = []
    q = []
    p.append(math.exp(-mean))
    q.append(p[0])
    x_max = int(mean + 6.0 * math.sqrt(mean) + 1.0)
    for i in range(1, x_max):
        last = p[-1]
        new = last * mean / float(i)
        p.append(new)
        q.append(q[-1] + new)
    return p, q

def get_poisson_random(p, q):
    u = random.random()
    k = 0
    last = q[k]
    while u >= last:
        k += 1
        last = q[k]
    return k

def main():
    c0 = 300000  #一回あたりの発注費用円]
    c1 = 1000    #商品一個、1日あたりの保管費用[円]
    c2 = 30000   #商品一個、1日あたりの品切れ損失費用[円]
    mean_demand_quantity = 10     #日々の需要量の平均[個]
    lead_time = 2                 #リードタイム
    order_quantity = 0            #発注量
    order_cycle = 20    #発注サイクル[日]
    safety_stock = 1    #安全在庫[個]
    c_list = []         #総在庫費用のリスト
    p, q = create_pdf(mean_demand_quantity)

    n = 200     #シミュレーション日数
    safety_stock_max = 10000    #安全在庫の最大値

    with tqdm(total=safety_stock_max) as pbar:
        while safety_stock <= safety_stock_max:
            n0 = 0      #総発注回数
            n1 = 0      #総保管個数
            n2 = 0      #総欠品個数
            deliver = 0     #入庫日
            x = math.ceil(lead_time * mean_demand_quantity + safety_stock)     #在庫量を初期在庫量に設定
            day = 1
            loop_count_day = 1  #発注サイクルをカウントする

            while day <= n:
                #入庫
                if day == deliver:          #入庫日を判定
                    x += order_quantity     #入庫分を在庫量に追加
                
                #出庫
                #demand = get_poisson_random(p, q)  #需要量(ポアソン分布から乱数)
                demand = np.random.poisson(mean_demand_quantity)
                rest = x - demand   #開始時の在庫量と需要量の差
                
                if rest >= 0:   #差が0以上
                    n1 += rest  #差を総保管個数に加算
                    x = rest    #終了時の在庫数を設定
                
                else:           #差が負
                    n2 += -rest #総欠品数を加算
                    x = 0       #終了時の在庫数を0に設定
                
                #発注
                if loop_count_day % order_cycle == 0:
                    deliver = day + lead_time
                    n0 += 1
                    order_quantity = mean_demand_quantity * (order_cycle + lead_time) + safety_stock - x
                
                day += 1
                if loop_count_day % order_cycle == 0:
                    loop_count_day = 0
                else:
                    loop_count_day += 1
            
            c_temp = c0*n0 + c1*n1 + c2*n2
            #print('安全在庫:{}, 総在庫費用:{}'.format(safety_stock, c_temp))
            safety_stock += 1
            c_list.append(c_temp)
            pbar.update(1)

    #得られたデータをcsvへ書き込む
    with open('./E2-1-2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['SafetyStock', 'AllStockCost'])
        for i in range(safety_stock_max):
            writer.writerow([i+1, c_list[i]])

if __name__ == '__main__':
    main()
