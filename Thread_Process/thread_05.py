from queue import Queue
from random import randint
from threading import Thread


def producer(out_q):
    while True:
        data = randint(0, 100)
        out_q.put(data)


def consumer(in_q):
    while True:
        data = in_q.get()
        print('consumer --> ', data)


q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q, ))
t1.start()
t2.start()