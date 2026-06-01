METADATA = {
    "id": 155,
    "name": "Min Stack",
    "slug": "min-stack",
    "category": "Design",
    "aliases": [],
    "tags": ["stack", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.",
}

class MinStack:
    """
    A stack data structure that supports all standard stack operations 
    plus a method to retrieve the minimum element in O(1) time.
    """

    def __init__(self) -> None:
        """
        Initializes the MinStack with two internal lists.
        One list stores the actual values, and the other stores the 
        minimum value present in the stack at that specific height.
        """
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        """
        Pushes the element val onto the stack.

        Args:
            val (int): The integer value to be pushed onto the stack.

        Examples:
            >>> ms = MinStack()
            >>> ms.push(-2)
            >>> ms.push(0)
            >>> ms.push(-3)
            >>> ms.getMin()
            -3
        """
        self.stack.append(val)
        
        # If min_stack is empty, the current value is the minimum.
        # Otherwise, the new minimum is the lesser of the current value 
        # and the previous minimum stored at the top of min_stack.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(val, current_min))

    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        """
        Gets the top element of the stack.

        Returns:
            int: The value of the top element.

        Examples:
            >>> ms = MinStack()
            >>> ms.push(2)
            >>> ms.top()
            2
        """
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.

        Returns:
            int: The minimum element currently in the stack.

        Examples:
            >>> ms = MinStack()
            >>> ms.push(2)
            >>> ms.push(0)
            >>> ms.push(3)
            >>> ms.getMin()
            0
        """
        return self.min_stack[-1]

def solve() -> None:
    """
    Entry point for testing the MinStack implementation.
    """
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
    print("All test cases passed!")
