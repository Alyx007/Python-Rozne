import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, turn_lock, current_turn, total_philosophers, eat_count, eat_lock):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.turn_lock = turn_lock
        self.current_turn = current_turn
        self.total_philosophers = total_philosophers
        self.eat_count = eat_count
        self.eat_lock = eat_lock

    def run(self):
        while True:
            self.think()
            self.pickup_forks()
            self.eat()
            self.putdown_forks()
            if self.check_eat_count():
                break

    def think(self):
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(1)

    def pickup_forks(self):
        while True:
            with self.turn_lock:
                if self.current_turn[0] == self.index:
                    self.left_fork.acquire()
                    self.right_fork.acquire()
                    return
            time.sleep(0.1)

    def eat(self):
        print(f"Philosopher {self.index} is eating.")
        time.sleep(1)
        with self.eat_lock:
            self.eat_count[self.index] += 1

    def putdown_forks(self):
        self.right_fork.release()
        self.left_fork.release()
        with self.turn_lock:
            self.current_turn[0] = (self.current_turn[0] + 1) % self.total_philosophers

    def check_eat_count(self):
        with self.eat_lock:
            if all(count >= 3 for count in self.eat_count):
                return True
        return False

# Number of philosophers
num_philosophers = 5

# Create forks (semaphores)
forks = [threading.Semaphore(1) for _ in range(num_philosophers)]

# Initial turn and turn lock
turn_lock = threading.Lock()
current_turn = [0]  # Using a list to make it mutable

# Eat count and eat lock
eat_count = [0] * num_philosophers
eat_lock = threading.Lock()

# Create philosophers
philosophers = [
    Philosopher(i, forks[i], forks[(i + 1) % num_philosophers], turn_lock, current_turn, num_philosophers, eat_count, eat_lock)
    for i in range(num_philosophers)
]

# Start threads
for p in philosophers:
    p.start()

# Wait for all threads to finish
for p in philosophers:
    p.join()

print("All philosophers have eaten at least 3 times.")
