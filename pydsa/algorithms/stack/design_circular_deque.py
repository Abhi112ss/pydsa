METADATA = {
    "id": 641,
    "name": "Design Circular Deque",
    "slug": "design-circular-deque",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "queue", "array"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(k)",
    "description": "Design a data structure that supports adding and removing elements from both ends in constant time.",
}

class MyCircularDeque:
    """
    A circular deque implementation using a fixed-size array and two pointers.
    """

    def __init__(self, k: int) -> None:
        """
        Initializes the deque with a maximum capacity of k.

        Args:
            k (int): The maximum number of elements the deque can hold.
        """
        self.capacity = k
        self.queue = [0] * k
        self.size = 0
        self.front = 0
        self.rear = k - 1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.

        Args:
            value (int): The value to be added.

        Returns:
            bool: True if successful, False otherwise.

        Examples:
            >>> dq = MyCircularDeque(3)
            >>> dq.insertFront(1)
            True
        """
        if self.size == self.capacity:
            return False
        
        # Move front pointer backward circularly
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.

        Args:
            value (int): The value to be added.

        Returns:
            bool: True if successful, False otherwise.
        """
        if self.size == self.capacity:
            return False
        
        # Move rear pointer forward circularly
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.

        Returns:
            bool: True if successful, False otherwise.
        """
        if self.size == 0:
            return False
        
        # Move front pointer forward circularly
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.

        Returns:
            bool: True if successful, False otherwise.
        """
        if self.size == 0:
            return False
        
        # Move rear pointer backward circularly
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Gets the front item from the deque. If the deque is empty, return -1.

        Returns:
            int: The front item or -1 if empty.
        """
        return self.queue[self.front] if self.size > 0 else -1

    def getRear(self) -> int:
        """
        Gets the last item from the deque. If the deque is empty, return -1.

        Returns:
            int: The last item or -1 if empty.
        """
        return self.queue[self.rear] if self.size > 0 else -1

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.

        Returns:
            bool: True if full, False otherwise.
        """
        return self.size == self.capacity

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self.size == 0


def solve() -> None:
    """
    Example usage of the MyCircularDeque class.
    """
    dq = MyCircularDeque(3)
    print(dq.insertLast(1))    # True
    print(dq.insertLast(2))    # True
    print(dq.insertFront(3))   # True
    print(dq.insertFront(4))   # False (capacity reached)
    print(dq.getRear())        # 2
    print(dq.isFull())         # True
    print(dq.getFront())       # 3
    print(dq.deleteLast())     # True
    print(dq.deleteFront())    # True
    print(dq.isEmpty())        # False
