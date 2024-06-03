import threading

class Philosopher(threading.Thread):
    def __init__(self, index, left_fork, right_fork, max_philosophers, meals_eaten):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.max_philosophers = max_philosophers
        self.meals_eaten = meals_eaten

    def run(self):
        while True:
            self.think()
            self.max_philosophers.acquire()
            self.left_fork.acquire()
            self.right_fork.acquire()
            self.eat()
            self.right_fork.release()
            self.left_fork.release()
            self.max_philosophers.release()
            self.meals_eaten[self.index] += 1
            if all(meal_count >= 1 for meal_count in self.meals_eaten):
                break

    def think(self):
        print(f"Philosopher {self.index} is thinking.")

    def eat(self):
        print(f"Philosopher {self.index} is eating.")

# Semaphores for the forks
forks = [threading.Semaphore(1) for _ in range(5)]
# Semaphore to limit the number of philosophers that can try to eat simultaneously
max_philosophers = threading.Semaphore(4)
# Counter to track how many times each philosopher has eaten
meals_eaten = [0] * 5

philosophers = [Philosopher(i, forks[i], forks[(i + 1) % 5], max_philosophers, meals_eaten) for i in range(5)]
for p in philosophers:
    p.start()
