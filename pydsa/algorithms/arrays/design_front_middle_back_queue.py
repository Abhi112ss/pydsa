METADATA = {
    "id": 1670,
    "name": "Design Front Middle Back Queue",
    "slug": "design_front_middle_back_queue",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "deque"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Implement a queue supporting push and pop operations at front, middle, and back in O(1) time.",
}


from collections import deque
from typing import Deque, List


class FrontMiddleBackQueue:
    """Queue supporting O(1) push/pop at front, middle, and back.

    The queue is split into two halves:
        * _left  holds the first ⌈n/2⌉ elements,
        * _right holds the remaining elements.
    The middle element is defined as the last element of _left.
    Rebalancing after each operation keeps the size invariant:
        len(_left) == len(_right)   or   len(_left) == len(_right) + 1
    """

    def __init__(self) -> None:
        self._left: Deque[int] = deque()
        self._right: Deque[int] = deque()

    def _rebalance(self) -> None:
        """Restore the size invariant between the two halves."""
        # Ensure left is never smaller than right
        while len(self._left) < len(self._right):
            self._left.append(self._right.popleft())
        # Ensure left is at most one element larger than right
        while len(self._left) > len(self._right) + 1:
            self._right.appendleft(self._left.pop())

    def pushFront(self, val: int) -> None:
        """Insert val at the front of the queue."""
        self._left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        """Insert val in the middle of the queue."""
        self._left.append(val)  # middle is the end of left half
        self._rebalance()

    def pushBack(self, val: int) -> None:
        """Insert val at the back of the queue."""
        self._right.append(val)
        self._rebalance()

    def popFront(self) -> int:
        """Remove and return the front element; return -1 if empty."""
        if not self._left and not self._right:
            return -1
        if self._left:
            result = self._left.popleft()
        else:
            result = self._right.popleft()
        self._rebalance()
        return result

    def popMiddle(self) -> int:
        """Remove and return the middle element; return -1 if empty."""
        if not self._left and not self._right:
            return -1
        result = self._left.pop()
        self._rebalance()
        return result

    def popBack(self) -> int:
        """Remove and return the back element; return -1 if empty."""
        if not self._left and not self._right:
            return -1
        if self._right:
            result = self._right.pop()
        else:
            result = self._left.pop()
        self._rebalance()
        return result


def solve() -> None:
    """Demonstrate usage of FrontMiddleBackQueue.

    Example:
        >>> q = FrontMiddleBackQueue()
        >>> q.pushFront(1)   # [1]
        >>> q.pushBack(2)    # [1,2]
        >>> q.pushMiddle(3)  # [1,3,2]
        >>> q.popMiddle()    # returns 3, queue becomes [1,2]
        >>> q.popFront()     # returns 1, queue becomes [2]
        >>> q.popBack()      # returns 2, queue becomes []
        >>> q.popFront()     # returns -1 (empty)
    """
    # The function contains no I/O; it simply runs the example when called.
    queue = FrontMiddleBackQueue()
    queue.pushFront(1)
    queue.pushBack(2)
    queue.pushMiddle(3)
    assert queue.popMiddle() == 3
    assert queue.popFront() == 1
    assert queue.popBack() == 2
    assert queue.popFront() == -1
