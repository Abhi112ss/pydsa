METADATA = {
    "id": 1756,
    "name": "Design Most Recently Used Queue",
    "slug": "design-most-recently-used-queue",
    "category": "Design",
    "aliases": [],
    "tags": ["doubly_linked_list", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a data structure that supports adding elements, removing the oldest element, and moving the most recently used element to the end of the queue.",
}

class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None

class MostRecentlyUsedQueue:
    def __init__(self, capacity: int):
        """
        Args:
            capacity (int): The maximum number of elements the queue can hold.
        """
        self.capacity = capacity
        self.lookup = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: Node) -> None:
        """
        Args:
            node (Node): The node to be removed from the linked list.
        """
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node) -> None:
        """
        Args:
            node (Node): The node to be added to the end of the list.
        """
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def add(self, value: int) -> None:
        """
        Args:
            value (int): The value to add to the queue.
        """
        if value in self.lookup:
            node = self.lookup[value]
            self._remove_node(node)
            self._add_to_tail(node)
        else:
            if len(self.lookup) == self.capacity:
                oldest_node = self.head.next
                del self.lookup[oldest_node.val]
                self._remove_node(oldest_node)
            
            new_node = Node(value)
            self.lookup[value] = new_node
            self._add_to_tail(new_node)

    def remove(self, value: int) -> None:
        """
        Args:
            value (int): The value to remove from the queue.
        """
        if value in self.lookup:
            node = self.lookup[value]
            self._remove_node(node)
            del self.lookup[value]

    def pop(self) -> int:
        """
        Args:
            None

        Returns:
            int: The value of the oldest element in the queue.
        """
        oldest_node = self.head.next
        val = oldest_node.val
        self._remove_node(oldest_node)
        del self.lookup[val]
        return val

def solve():
    pass