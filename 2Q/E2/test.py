import simpy
import numpy as np
import random

# 到着イベント
def arrive():
    global time, stay, canserve
    while True:
        yield env.timeout(random.expovariate(0.2)) # 平均到着率 
        time.append(env.now)
        stay += 1
        if(canserve):
            env.process(queue())

# 待ち行列に並ぶ
def queue():
    global stay, stay_time, time, canserve
    canserve = False
    while len(time) > 0:
        yield env.timeout(random.expovariate(2.0)) # 平均サービス率
        stay_time += env.now - time[0]
        time = time[1:]
        stay -= 1 #店から出た
    canserve = True
    
time = [0] #客が出入りしたときの時刻
stay = 0 #客の滞在人数
stay_time = 0 #滞在人数×滞在時間
canserve = True
    
#客の到着率、サービス率は指数分布に従う
env = simpy.Environment()

# 実行
env.process(arrive())
env.run(until = 1000)

#print(np.average(stay_time))
print(np.sum(stay_time)/1000)