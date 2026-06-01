METADATA = {
    "id": 1188,
    "name": "Design Bounded Blocking Queue",
    "slug": "design-bounded-blocking-queue",
    "category": "Concurrency",
    "aliases": [],
    "tags": ["concurrency", "queue", "threading"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(capacity)",
    "description": "Implement a thread-safe bounded blocking queue that supports enqueue and dequeue operations with blocking behavior.",
}

import threading
from collections import deque

class BoundedBlockingQueue:
    """
    A thread-safe bounded blocking queue implementation.
    
    This queue has a fixed capacity. If the queue is full, enqueue operations 
    will block until space becomes available. If the queue is empty, 
    dequeue operations will block until an item is added.
    """

    def __init__(self, capacity: int):
        """
        Initializes the queue with a specific capacity.

        Args:
            capacity (int): The maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.queue = deque()
        
        # Lock to protect access to the internal deque
        self.lock = threading.Lock()
        
        # Condition variable to manage blocking/notifying threads
        # We use one condition variable to manage both 'not full' and 'not empty' states
        self.condition = threading.Condition(self.lock)

    def enqueue(self, value: int) -> None:
        """
        Adds an element to the end of the queue. 
        Blocks if the queue is at capacity.

        Args:
            value (int): The integer value to be added to the queue.
        """
        with self.condition:
            # Wait while the queue is at its maximum capacity
            while len(self.queue) == self.capacity:
                self.condition.wait()
            
            self.queue.append(value)
            
            # Notify any waiting dequeue threads that the queue is no longer empty
            self.condition.notify_all()

    def dequeue(self) -> int:
        """
        Removes and returns the element from the front of the queue.
        Blocks if the queue is empty.

        Returns:
            int: The element removed from the front of the queue.
        """
        with self.condition:
            # Wait while the queue is empty
            while len(self.queue) == 0:
                self.condition.wait()
            
            value = self.queue.popleft()
            
            # Notify any waiting enqueue threads that space has become available
            self.condition.notify_all()
            return value

def solve():
    """
    Example usage of the BoundedBlockingQueue.
    """
    queue = BoundedBlockingQueue(2)

    def producer():
        for i in range(5):
            print(f"Producer attempting to enqueue: {i}")
            queue.enqueue(i)
            print(f"Producer enqueued: {i}")

    def consumer():
        for i in range(5):
            import time
            time.sleep(1)  # Simulate processing time
            val = queue.dequeue()
            print(f"Consumer dequeued: {val}")

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
