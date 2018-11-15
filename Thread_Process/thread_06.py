from queue import Queue
from random import randint
from threading import Thread


# A thread that produces data
def producer(out_q):
    i = 0
    while True:
        # Produce some data
        data = i
        out_q.put(data)
        i += 1


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        # Process the data
        print('consumer --> ', data)
        # Indicate completion
        in_q.task_done()


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# Wait for all produced items to be consumed
q.join()
