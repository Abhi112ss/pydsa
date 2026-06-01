METADATA = {
    "id": 146,
    "name": "LRU Cache",
    "slug": "lru_cache",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "doubly_linked_list", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(capacity)",
    "description": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.",
}

class Node:
    """A node in a doubly linked list."""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    """
    LRU Cache implementation using a Hash Map and a Doubly Linked List.
    
    The Hash Map provides O(1) access to nodes, while the Doubly Linked List
    maintains the order of usage. The most recently used items are kept at 
    the 'head', and the least recently used items are at the 'tail'.
    """

    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with a specific capacity.

        Args:
            capacity (int): The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        
        # Dummy head and tail to simplify edge cases (insertion/deletion)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Removes a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _add_to_front(self, node: Node) -> None:
        """Adds a node right after the dummy head (most recent position)."""
        first_real_node = self.head.next
        
        self.head.next = node
        node.prev = self.head
        node.next = first_real_node
        
        if first_real_node:
            first_real_node.prev = node

    def _move_to_front(self, node: Node) -> None:
        """Moves an existing node to the front of the list."""
        self._remove(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        """
        Returns the value of the key if it exists, otherwise -1.
        Updates the key as most recently used.

        Args:
            key (int): The key to look up.

        Returns:
            int: The value associated with the key, or -1 if not found.
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates the value of the key. 
        If the cache reaches capacity, it evicts the least recently used item.

        Args:
            key (int): The key to insert or update.
            value (int): The value to associate with the key.
        """
        if key in self.cache:
            # Update existing key and move to front
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # Create new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
            
            # Check if capacity exceeded
            if len(self.cache) > self.capacity:
                # Evict the least recently used (node before dummy tail)
                lru_node = self.tail.prev
                if lru_node:
                    self._remove(lru_node)
                    del self.cache[lru_node.key]

def solve():
    """
    Example usage of the LRUCache implementation.
    """
    lru = LRUCache(2)
    lru.put(1, 1)  # cache is {1=1}
    lru.put(2, 2)  # cache is {1=1, 2=2}
    assert lru.get(1) == 1  # returns 1, cache is {2=2, 1=1}
    lru.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}
    assert lru.get(2) == -1  # returns -1 (not found)
    lru.put(4, 4)  # evicts key 1, cache is {3=3, 4=4}
    assert lru.get(1) == -1  # returns -1 (not found)
    assert lru.get(3) == 3  # returns 3
    assert lru.get(4) == 4  # returns 4
    print("All test cases passed!")
