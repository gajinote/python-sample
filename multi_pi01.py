# -*- coding: utf-8 -*-

import threading
import time
import datetime

def f(x):
    return 4 / (1.0 + x**2)

class TestThread(threading.Thread):
    def __init__(self, st, ed, step):
      super(TestThread, self).__init__()
      self.st=st
      self.ed=ed
      self.step = step
      self.return_value = None

    def run(self):
      sum = 0
      for i in range(self.st, self.ed):
        x = (i + 0.5) * self.step
        sum += f(x)
      # print("pi = " , sum * step)
      self.return_value = sum * step

    def get_value(self):
      return self.return_value

if __name__ == "__main__":
  start_t = time.time()
  pi = 0
  n = 10000000
  step = 1.0 / n
  sub_t1 = TestThread(0, int(n/2), step)
  sub_t2 = TestThread(int(n/2), n, step)
  sub_t1.start()
  sub_t2.start()
  # sub_t.join()
  while(sub_t1.is_alive() or sub_t2.is_alive()):
#    print("wait")
    time.sleep(1)
  pi = sub_t1.return_value + sub_t2.return_value
  end_t = time.time()
  elapsed_t = end_t - start_t
  print("pi = " , pi)
  print("execute time = ", str(elapsed_t))
 

