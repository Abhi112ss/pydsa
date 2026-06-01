METADATA = {
    "id": 622,
    "name": "Design Circular Queue",
    "slug": "design-circular-queue",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "queue", "array"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(k)",
    "description": "Design a data structure for a circular queue.",
}

class MyCircularQueue:
    """
    A circular queue implementation using a fixed-size list.
    
    The queue uses a head pointer, a tail pointer, and a current size 
    counter to manage the circular wrap-around logic efficiently.
    """

    def __init__(self, k: int):
        """
        Initialize the data structure with a fixed size k.

        Args:
            k (int): The maximum capacity of the queue.
        """
        self.capacity = k
        self.queue = [0] * k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue.

        Args:
            value (int): The value to be added.

        Returns:
            bool: True if the operation is successful, otherwise False.
        """
        if self.isFull():
            return False
        
        # Move tail forward using modulo to wrap around the array
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue.

        Returns:
            bool: True if the operation is successful, otherwise False.
        """
        if self.isEmpty():
            return False
        
        # Move head forward using modulo to wrap around the array
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.

        Returns:
            int: The front item, or -1 if the queue is empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.

        Returns:
            int: The last item, or -1 if the queue is empty.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self.size == self.capacity


def solve():
    """
    Example usage of the MyCircularQueue class.
    """
    # Example 1:
    # my_queue = MyCircularQueue(3)
    # my_queue.enQueue(1) -> True
    # my_queue.enQueue(2) -> True
    # my_queue.enQueue(3) -> True
    # my_queue.enQueue(4) -> False
    # my_queue.Rear() -> 3
    # my_queue.isFull() -> True
    # my_queue.deQueue() -> True
    # my_queue.enQueue(4) -> True
    # my_queue.Rear() -> 4
    
    q = MyCircularQueue(3)
    assert q.enQueue(1) is True
    assert q.enQueue(2) is True
    assert q.enQueue(3) is True
    assert q.enQueue(4) is False
    assert q.Rear() == 3
    assert q.isFull() is True
    assert q.deQueue() is True
    assert q.enQueue(4) is True
    assert q.Rear() == 4
    assert q.isEmpty() is False
    
    print("All test cases passed!")
