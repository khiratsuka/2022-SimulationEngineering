# 2112621-simE2-2.py
# 変数は適宜変更すること。

import random
import numpy as np
from tqdm import tqdm
import csv
import math

def main():
    lam = 0.2           #平均到着率[人/時間]
    mean_service = 2.0  #平均サービス率[人/時間]
    sim_end = 50000     #シミュレーション終了時刻
    lam_max = 1.9       #lambdaの最大値
    lam_delta = 0.1     #lambdaの上げ幅
    ave_x_list = []     #xの平均を入れるリスト
    lam_list = []       #lambdaを入れるリスト

    while lam <= lam_max:
        x = 0               #系内客数[人]
        sum_x = 0.0         #系内客数の和
        window = False      #窓口の状況 T:満席/F:空席
        timetable = []      #タイムテーブル(事象リスト)
        wait_list = []      #待ち行列

        t = 0.0
        dta = -lam * math.log(1-random.random())
        ev = [t+dta, "a"]
        timetable.append(ev)

        with tqdm(total=sim_end, desc='lambda={}'.format(str(lam))) as pbar:
            while t <= sim_end:
                ev = timetable.pop(0)
                t_last = t
                t = ev[0]
                #print('x:{}, (t - t_last):{}, x * (t - t_last):{}'.format(x, (t-t_last), x * (t - t_last)))    #debug
                sum_x += x * (t - t_last)
                
                #到着イベントの場合
                if ev[1] == "a":
                    #窓口が空席
                    if not window:
                        #print('arrive, not service')    #debug
                        window = True   #窓口を満席へ
                        x = 1          #系内客数を更新
                        dts = random.expovariate(mean_service)
                        timetable.append([t+dts, "d"])  #退去イベントを追加
                        dta = random.expovariate(lam)
                        timetable.append([t+dta, "a"])  #到着イベントを追加
                    
                    #窓口が満席
                    elif window:
                        #print('arrive, service')    #debug
                        wait_list.append("a")   #待ち行列に追加
                        x += 1                  #系内客数を更新
                        dta = random.expovariate(lam)
                        timetable.append([t+dta, "a"])  #到着イベントを追加
                
                #退去イベントの場合
                elif ev[1] == "d":
                    #待ち客が存在する
                    if len(wait_list) > 0:
                        #print('deperture, exist waiting customer') #debug
                        _ = wait_list.pop(0)    #待ち客を窓口へ入れる
                        window = True           #窓口を満席へ
                        x -= 1                  #系内客数を更新
                        dts = random.expovariate(mean_service)
                        timetable.append([t+dts, "d"])  #退去イベントを追加
                    
                    #待ち客が存在しない
                    elif len(wait_list) == 0:
                        #print('deperture, not exist waiting customer')  #debug
                        window = False          #窓口を空席へ
                        x -= 1
                else:
                    print('error time table: {}'.format(ev))
                
                timetable.sort()
                pbar.update(t-t_last)
        

        sum_x += x * (sim_end - t_last)
        ave_x_temp = sum_x / sim_end
        ave_x_list.append(ave_x_temp)
        lam_list.append(lam)
        print('lambda:{}, ave_x:{}'.format(lam, ave_x_temp))
        lam += lam_delta
        lam = round(lam, 1)
    
    #得られたデータをcsvへ書き込む
    with open('./E2-2-2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['lambda', 'average_customers', 'analytical solution'])
        i = 0
        for l, ave_x in zip(lam_list, ave_x_list):
            writer.writerow([l, ave_x, ((l/mean_service)/(1-(l/mean_service)))])


if __name__ == '__main__':
    main()