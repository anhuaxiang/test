# https://www.jqhtml.com/12844.html

import time
import threading
from threading import Thread


# def func(m, n):
#     thread_name = threading.current_thread().getName()
#     print(thread_name, "starting...")
#     for i in range(m, n):
#         print(thread_name, '--->', i)
#
#
# t1 = threading.Thread(target=func, args=(1, 500, ))
# t2 = threading.Thread(target=func, args=(500, 1000,))
# t1.start()
# t2.start()
# print("xxxxxxxxxxxxxxx")


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()  # Signal termination
t.join()  # Wait for actual termination (if needed)
