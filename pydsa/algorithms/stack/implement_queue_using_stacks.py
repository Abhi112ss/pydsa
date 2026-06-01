METADATA = {
    "id": 232,
    "name": "Implement Queue using Stacks",
    "slug": "implement_queue_using_stacks",
    "category": "Design",
    "aliases": [],
    "tags": ["stack", "queue", "design"],
    "difficulty": "easy",
    "time_complexity": "O(1) amortized",
    "space_complexity": "O(n)",
    "description": "Implements a FIFO queue using two LIFO stacks.",
}


class MyQueue:
    """Queue implemented with two stacks.

    The push operation appends to the `push_stack`.  When a pop or peek is
    requested and the `pop_stack` is empty, all elements are transferred from
    `push_stack` to `pop_stack`, reversing their order and enabling FIFO behavior.
    """

    def __init__(self) -> None:
        self._push_stack: list[int] = []  # Stack for incoming elements
        self._pop_stack: list[int] = []   # Stack for outgoing elements

    def push(self, x: int) -> None:
        """Push element `x` to the back of the queue."""
        self._push_stack.append(x)

    def _transfer(self) -> None:
        """Move all elements from the push stack to the pop stack."""
        while self._push_stack:
            self._pop_stack.append(self._push_stack.pop())

    def pop(self) -> int:
        """Remove and return the element from the front of the queue."""
        if not self._pop_stack:
            self._transfer()
        return self._pop_stack.pop()

    def peek(self) -> int:
        """Return the front element without removing it."""
        if not self._pop_stack:
            self._transfer()
        return self._pop_stack[-1]

    def empty(self) -> bool:
        """Return ``True`` if the queue is empty."""
        return not self._push_stack and not self._pop_stack


def solve() -> None:
    """Demonstrates usage of ``MyQueue``.

    Args:
        None

    Returns:
        None

    Example:
        >>> queue = MyQueue()
        >>> queue.push(1)
        >>> queue.push(2)
        >>> queue.peek()
        1
        >>> queue.pop()
        1
        >>> queue.empty()
        False
    """
    # No input/output required for this design problem.
    pass