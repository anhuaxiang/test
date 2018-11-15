import threading
from Thread_Process.thread_08 import acquire


def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(threading.current_thread().getName() + ' eating \n')


NSTICKS = 5
chopsticks = [threading.Lock() for i in range(NSTICKS)]

for i in range(NSTICKS):
    t = threading.Thread(target=philosopher, args=(chopsticks[i], chopsticks[(i+1) % NSTICKS]))
    t.start()
