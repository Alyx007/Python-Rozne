import threading

class DiningPhilosophers:
    def __init__(self):
        self.lock = threading.Lock()
        self.conditions = [threading.Condition(self.lock) for _ in range(5)]
        self.states = ['thinking'] * 5

    def pickup(self, i):
        with self.lock:
            self.states[i] = 'hungry'
            self._test(i)
            if self.states[i] != 'eating':
                self.conditions[i].wait()

    def putdown(self, i):
        with self.lock:
            self.states[i] = 'thinking'
            self._test((i - 1) % 5)
            self._test((i + 1) % 5)

    def _test(self, i):
        if (self.states[i] == 'hungry' and 
            self.states[(i - 1) % 5] != 'eating' and
            self.states[(i + 1) % 5] != 'eating'):
            self.states[i] = 'eating'
            self.conditions[i].notify()

    def philosopher(self, i):
        while True:
            self.pickup(i)
            print(f"Philosopher {i} is eating.")
            self.putdown(i)
            print(f"Philosopher {i} is thinking.")

dining_philosophers = DiningPhilosophers()
philosophers = [threading.Thread(target=dining_philosophers.philosopher, args=(i,)) for i in range(5)]
for p in philosophers:
    p.start()
