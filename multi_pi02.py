# -*- coding:utf-8 -*-

import time
import datetime

from multiprocessing import Pool
from collections import Counter

def f(x):
    return 4 / ( 1.0 + x**2 )

# multiprocess
def multi_func(st_x, st_y, step):
    sum = 0
    for i in range(int(st_x), int(st_y)):
        x = (i + 0.5) * step
        sum += f(x)
    # print(sum)
    return sum

def wrapper(args):
    return multi_func(*args)

def multi_process(sampleList):
    # Procecc Num:8
    p = Pool(4)
    output = p.map(wrapper, sampleList)
    # process End
    p.close()
    return output

if __name__=="__main__":

    # n回の処理を並列処理
    num = 10000000
    p_num = 4
    pi = 0
    step = 1.0 / num
    sumpleList=[]

    start_t = time.time()
    sampleList= [(i*num/4, (i+1)*num/4, step ) for i in range(p_num)]

    output = multi_process(sampleList)
    end_t = time.time()
    for i in range(len(output)):
        pi += output[i]
    pi *= step


    elapsed_t = end_t - start_t
    print("pi = ", str(pi))
    print("execut time:", str(elapsed_t))
