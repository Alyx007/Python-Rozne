import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, turn_lock, current_turn, total_philosophers):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.turn_lock = turn_lock
        self.current_turn = current_turn
        self.total_philosophers = total_philosophers

    def run(self):
        while True:
            self.think()
            self.pickup_forks()
            self.eat()
            self.putdown_forks()

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

    def putdown_forks(self):
        self.right_fork.release()
        self.left_fork.release()
        with self.turn_lock:
            self.current_turn[0] = (self.current_turn[0] + 1) % self.total_philosophers

# Número de filósofos
num_philosophers = 5

# Creación de tenedores (semaforos)
forks = [threading.Semaphore(1) for _ in range(num_philosophers)]

# Turno inicial y bloqueo del turno
turn_lock = threading.Lock()
current_turn = [0]  # Usamos una lista para que sea mutable

# Creación de los filósofos
philosophers = [
    Philosopher(i, forks[i], forks[(i + 1) % num_philosophers], turn_lock, current_turn, num_philosophers)
    for i in range(num_philosophers)
]

# Inicio de los hilos
for p in philosophers:
    p.start()
