METADATA = {
    "id": 1226,
    "name": "The Dining Philosophers",
    "slug": "the-dining-philosophers",
    "category": "Concurrency",
    "aliases": [],
    "tags": ["concurrency", "logic", "deadlock-prevention"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Simulate a dining philosopher scenario where philosophers must pick up two forks without causing a deadlock.",
}

import threading
import time

class DiningPhilosopher:
    """
    A class to simulate the Dining Philosophers problem.
    
    The goal is to prevent deadlock by ensuring that not all philosophers 
    attempt to pick up their left fork at the same time. This is achieved 
    by using a semaphore to limit the number of philosophers allowed to 
    attempt to eat simultaneously to N-1.
    """

    def __init__(self, n: int):
        """
        Initializes the dining philosopher simulation.

        Args:
            n (int): The number of philosophers and forks.
        """
        self.n = n
        # Each fork is represented by a lock
        self.forks = [threading.Lock() for _ in range(n)]
        # Semaphore to limit active philosophers to n-1 to prevent circular wait (deadlock)
        self.limiter = threading.Semaphore(n - 1)
        self.results = []
        self.results_lock = threading.Lock()

    def _eat(self, philosopher_id: int):
        """
        The routine for a single philosopher.

        Args:
            philosopher_id (int): The unique ID of the philosopher.
        """
        # Step 1: Acquire permission from the limiter to prevent deadlock
        with self.limiter:
            left_fork = philosopher_id
            right_fork = (philosopher_id + 1) % self.n

            # Step 2: Acquire both forks (locks)
            # We always pick up the lower-indexed fork first to further prevent deadlock
            first_fork, second_fork = sorted([left_fork, right_fork])

            with self.forks[first_fork]:
                with self.forks[second_fork]:
                    # Simulate eating
                    time.sleep(0.01)
                    with self.results_lock:
                        self.results.append(philosopher_id)

    def solve(self, eat_counts: list[int]) -> list[int]:
        """
        Starts the simulation where each philosopher eats a specific number of times.

        Args:
            eat_counts (list[int]): A list where eat_counts[i] is the number of 
                times philosopher i must eat.

        Returns:
            list[int]: The order in which philosophers finished eating.

        Examples:
            >>> dp = DiningPhilosopher(5)
            >>> dp.solve([1, 1, 1, 1, 1])
            [0, 1, 2, 3, 4] # (Order may vary due to concurrency)
        """
        threads = []
        
        # Create a thread for each philosopher's eating requirement
        for philosopher_id, count in enumerate(eat_counts):
            def philosopher_task(p_id: int, c: int):
                for _ in range(c):
                    self._eat(p_id)
            
            # We create a thread that handles all eating cycles for one philosopher
            t = threading.Thread(target=philosopher_task, args=(philosopher_id, count))
            threads.append(t)
            t.start()

        # Wait for all philosophers to finish eating
        for t in threads:
            t.join()

        return self.results

def solve(n: int, eat_counts: list[int]) -> list[int]:
    """
    Entry point function to solve the Dining Philosophers problem.

    Args:
        n (int): Number of philosophers.
        eat_counts (list[int]): Number of times each philosopher eats.

    Returns:
        list[int]: The sequence of philosophers who finished eating.
    """
    simulator = DiningPhilosopher(n)
    return simulator.solve(eat_counts)
