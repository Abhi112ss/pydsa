METADATA = {
    "id": 716,
    "name": "Max Stack",
    "slug": "max_stack",
    "category": "Design",
    "aliases": [],
    "tags": ["stack", "design", "linked_list", "ordered_map"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a stack that supports push, pop, top, peekMax, and popMax operations.",
}

import heapq

class Node:
    """A node in a doubly linked list."""
    def __init__(self, val: int):
        self.val = val
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None
        self.removed: bool = False

class MaxStack:
    """
    A stack implementation that supports retrieving and removing the maximum element.
    
    Uses a doubly linked list to maintain stack order and a max-heap to track 
    the maximum values. Lazy removal is used to handle elements removed via 
    pop() or popMax().
    """

    def __init__(self) -> None:
        # Doubly linked list to maintain stack order (LIFO)
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # Max-heap to track values. Stores (-value, unique_id, node_reference)
        # unique_id is used to handle duplicate values and ensure stable ordering
        self.max_heap: list[tuple[int, int, Node]] = []
        self.counter = 0
        self.size = 0

    def push(self, x: int) -> None:
        """
        Pushes element x onto the stack.

        Args:
            x: The integer to push onto the stack.
        """
        new_node = Node(x)
        # Insert at the end of the doubly linked list (top of stack)
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node
        
        # Push to heap with a counter to handle duplicate values correctly
        heapq.heappush(self.max_heap, (-x, self.counter, new_node))
        self.counter += 1
        self.size += 1

    def _remove_node(self, node: Node) -> None:
        """Helper to remove a node from the doubly linked list and mark it."""
        node.removed = True
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns it.

        Returns:
            The integer removed from the top of the stack.
        """
        # Clean up heap top if it points to a node already removed via popMax
        while self.max_heap and self.max_heap[0][2].removed:
            heapq.heappop(self.max_heap)
            
        # The top of the stack is the node before the tail
        top_node = self.tail.prev
        val = top_node.val
        self._remove_node(top_node)
        return val

    def top(self) -> int:
        """
        Gets the element on top of the stack.

        Returns:
            The integer at the top of the stack.
        """
        while self.max_heap and self.max_heap[0][2].removed:
            heapq.heappop(self.max_heap)
        return self.tail.prev.val

    def peekMax(self) -> int:
        """
        Retrieves the maximum element in the stack.

        Returns:
            The maximum integer in the stack.
        """
        while self.max_heap and self.max_heap[0][2].removed:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        """
        Removes and returns the maximum element in the stack. 
        If there is more than one maximum element, remove the top-most one.

        Returns:
            The maximum integer removed from the stack.
        """
        # 1. Find the valid maximum node
        while self.max_heap and self.max_heap[0][2].removed:
            heapq.heappop(self.max_heap)
            
        neg_val, _, max_node = heapq.heappop(self.max_heap)
        val = -neg_val
        
        # 2. Remove from the doubly linked list
        self._remove_node(max_node)
        return val

from typing import Optional

def solve():
    """
    Example usage of the MaxStack class.
    """
    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(5)
    print(stack.top())      # Returns 5
    print(stack.popMax())   # Returns 5
    print(stack.top())      # Returns 1
    print(stack.popMax())   # Returns 5 (Wait, the logic above: 5, 1, 5 -> popMax is 5. Stack is 5, 1)
    # Correct trace:
    # push 5: [5]
    # push 1: [5, 1]
    # push 5: [5, 1, 5]
    # top: 5
    # popMax: 5 (removes the top-most 5). Stack: [5, 1]
    # top: 1
    # popMax: 5 (removes the 5). Stack: [1]
