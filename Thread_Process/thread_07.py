from queue import Queue
from random import randint
from threading import Thread, Event


# A thread that produces data
def producer(out_q):
    i = 0
    while True:
        # Produce some data
        data = randint(1, 10)
        # Make an (data, event) pair and hand it to the consumer
        evt = Event()
        out_q.put((i, evt))
        # Wait for the consumer to process the item
        evt.wait()
        i += 1


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data, evt = in_q.get()
        # Process the data
        print(data)
        # Indicate completion
        evt.set()


q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()