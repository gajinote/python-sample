# -*- coding: utf-8 -*-
import time

def f(x):
  return 4 / (1.0 + x**2)

start_t = time.time()
n = 10000000
sum = 0
step = 1.0 / n

for i in range(0, n):
  x = (i + 0.5) * step
  sum += f(x)

pi = sum * step

end_t = time.time()

elapsed_t = end_t - start_t

print("pi = " , str(pi))
print("execute time:", str(elapsed_t))

# print("elapsed_time: {0}".format(elapsed_t))
