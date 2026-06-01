METADATA = {
    "id": 1381,
    "name": "Design a Stack With Increment Operation",
    "slug": "design-a-stack-with-increment-operation",
    "category": "Design",
    "aliases": [],
    "tags": ["stack", "design", "array"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a stack that supports push, pop, and an increment operation on the bottom k elements.",
}

class CustomStack:
    """
    A stack implementation that supports an efficient increment operation
    on the bottom k elements using lazy propagation.
    """

    def __init__(self, maxSize: int):
        """
        Initializes the stack with a maximum size.

        Args:
            maxSize (int): The maximum number of elements the stack can hold.
        """
        self.max_size = maxSize
        self.stack = []
        # increments[i] stores the increment value to be applied to stack[i]
        # and all elements below it.
        self.increments = []

    def push(self, x: int) -> None:
        """
        Pushes an element onto the stack if the stack has not reached maxSize.

        Args:
            x (int): The integer to push onto the stack.
        """
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns it.

        Returns:
            int: The top element of the stack, or -1 if the stack is empty.
        """
        if not self.stack:
            return -1

        # Get the index of the top element
        index = len(self.stack) - 1
        
        # Retrieve the value and add the accumulated increment for this position
        val = self.stack.pop() + self.increments[index]
        self.increments.pop()

        # Lazy propagation: pass the increment down to the next element below
        if index > 0:
            self.increments[index - 1] += self.increments[index]

        return val

    def increment(self, k: int, inc: int) -> None:
        """
        Increments the bottom k elements of the stack by inc.

        Args:
            k (int): The number of bottom elements to increment.
            inc (int): The value to add to each of the k elements.
        """
        if not self.stack:
            return

        # We only increment up to the minimum of k or the current stack size
        # We apply the increment to the k-th element (or the top-most available)
        # to ensure O(1) complexity via lazy propagation.
        idx = min(k, len(self.stack)) - 1
        self.increments[idx] += inc

def solve():
    """
    Example usage of the CustomStack class.
    """
    # Example 1:
    # obj = CustomStack(5)
    # obj.push(1)
    # obj.push(2)
    # obj.push(3)
    # obj.increment(2, 100)
    # print(obj.pop()) # returns 3
    # print(obj.pop()) # returns 102
    pass
