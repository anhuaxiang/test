import threading


class ShareCounter:
    def __init__(self, initial_value):
        self._initial_value = initial_value
        self._lock = threading.Lock()

    def increment(self, delta=1):
        self._lock.acquire()
        self._initial_value += delta
        print(self._initial_value)
        self._lock.release()

    def decrement(self, delta=1):
        self._lock.acquire()
        self._initial_value -= delta
        print(self._initial_value)
        self._lock.release()


class ShareCounterAsWith:
    def __init__(self, initial_value):
        self._initial_value = initial_value
        self._lock = threading.Lock()

    def increment(self, delta=1):
        with self._lock:
            self._initial_value += delta
            print(self._initial_value)

    def decrement(self, delta=1):
        with self._lock:
            self._initial_value -= delta
            print(self._initial_value)


sc = ShareCounter(5)
threading.Thread(target=sc.decrement).start()
threading.Thread(target=sc.increment).start()
print(sc._initial_value)

sc1 = ShareCounterAsWith(10)
threading.Thread(target=sc1.decrement).start()
threading.Thread(target=sc1.increment).start()
print(sc1._initial_value)