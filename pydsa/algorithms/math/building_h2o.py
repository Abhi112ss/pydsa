METADATA = {
    "id": 1117,
    "name": "Building H2O",
    "slug": "building-h2o",
    "category": "Concurrency",
    "aliases": [],
    "tags": ["concurrency", "synchronization", "threading", "semaphore"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(1)",
    "description": "Use semaphores to control the release of hydrogen and oxygen threads to form H2O molecules.",
}

import threading

class H2O:
    def __init__(self) -> None:
        """
        Initializes the H2O object with semaphores to control thread flow.
        
        We need to ensure that for every 3 threads (2 Hydrogen, 1 Oxygen), 
        they are released to form a molecule.
        """
        # Limits the number of hydrogen threads that can proceed
        self.hydrogen_semaphore = threading.Semaphore(2)
        # Limits the number of oxygen threads that can proceed
        self.oxygen_semaphore = threading.Semaphore(1)
        # A barrier to ensure all 3 threads of a group reach the point before proceeding
        self.barrier = threading.Barrier(3)

    def hydrogen(self, x: int) -> None:
        """
        Simulates a hydrogen thread.

        Args:
            x: An integer representing the thread identifier (unused in logic).
        
        Returns:
            None
            
        Examples:
            >>> h2o = H2O()
            >>> threading.Thread(target=h2o.hydrogen, args=(1,)).start()
        """
        # Wait for a slot in the current H2O molecule group
        self.hydrogen_semaphore.acquire()
        
        # Wait for the other two threads (1 H and 1 O) to arrive
        self.barrier.wait()
        
        # Release the slot for the next molecule's hydrogen
        self.hydrogen_semaphore.release()

    def oxygen(self, x: int) -> None:
        """
        Simulates an oxygen thread.

        Args:
            x: An integer representing the thread identifier (unused in logic).
        
        Returns:
            None
            
        Examples:
            >>> h2o = H2O()
            >>> threading.Thread(target=h2o.oxygen, args=(1,)).start()
        """
        # Wait for a slot in the current H2O molecule group
        self.oxygen_semaphore.acquire()
        
        # Wait for the other two threads (2 H) to arrive
        self.barrier.wait()
        
        # Release the slot for the next molecule's oxygen
        self.oxygen_semaphore.release()

# Note: The implementation uses a Barrier to synchronize the exact count of 3.
# The semaphores act as a throttle to ensure the ratio 2:1 is maintained.
# Even if many threads are called, the semaphores prevent more than 2H and 1O
# from entering the barrier at any single time.