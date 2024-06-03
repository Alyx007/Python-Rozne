import threading
import time

class Butler:
    def __init__(self, num_philosophers, max_meals):
        self.available = num_philosophers - 1
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.meals_eaten = [0] * num_philosophers
        self.max_meals = max_meals

    def wants_to_eat(self, philosopher_index):
        with self.lock:
            while self.available == 0 or self.meals_eaten[philosopher_index] >= self.max_meals:
                self.condition.wait()
            self.available -= 1

    def done_eating(self, philosopher_index):
        with self.lock:
            self.available += 1
            self.meals_eaten[philosopher_index] += 1
            self.condition.notify_all()

    def all_philosophers_done(self):
        with self.lock:
            return all(meals >= self.max_meals for meals in self.meals_eaten)

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, butler):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.butler = butler

    def run(self):
        while True:
            self.think()
            self.butler.wants_to_eat(self.index)
            self.pickup_forks()
            self.eat()
            self.putdown_forks()
            self.butler.done_eating(self.index)
            if self.butler.all_philosophers_done():
                break

    def think(self):
        print(f"Philosopher {self.index} is thinking.")
        time.sleep(1)

    def pickup_forks(self):
        self.left_fork.acquire()
        self.right_fork.acquire()

    def eat(self):
        print(f"Philosopher {self.index} is eating.")
        time.sleep(1)

    def putdown_forks(self):
        self.right_fork.release()
        self.left_fork.release()

# Número de filósofos y cenas
num_philosophers = 5
max_meals = 1

# Creación de tenedores (semaforos)
forks = [threading.Semaphore(1) for _ in range(num_philosophers)]

# Creación del Dijkstra
butler = Butler(num_philosophers, max_meals)

# Creación de los filósofos
philosophers = [
    Philosopher(i, forks[i], forks[(i + 1) % num_philosophers], butler)
    for i in range(num_philosophers)
]

# Inicio de los hilos
for p in philosophers:
    p.start()

# Espera a que todos los hilos terminen
for p in philosophers:
    p.join()

print("All philosophers have eaten 3 times.")

