METADATA = {
    "id": 432,
    "name": "All O`one Data Structure",
    "slug": "all_o_one_data_structure",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "doubly_linked_list", "design"],
    "difficulty": "hard",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a data structure that supports inc, dec, getMax, and getMin operations in constant time.",
}

class Node:
    """A node in the doubly linked list representing a frequency bucket."""
    def __init__(self, count: int):
        self.count = count
        self.keys: set[str] = set()
        self.prev: "Node" = None
        self.next: "Node" = None

class AllOne:
    """
    A data structure that maintains a set of strings and their frequencies.
    Uses a doubly linked list of frequency buckets and a hash map for O(1) access.
    """

    def __init__(self) -> None:
        # Map key -> Node containing that key
        self.key_to_node: dict[str, Node] = {}
        
        # Sentinel nodes for the doubly linked list
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node: Node, prev_node: Node) -> None:
        """Helper to insert a new node into the linked list."""
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node: Node) -> None:
        """Helper to remove a node from the linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        """
        Increments the count of the provided key by 1.
        
        Args:
            key: The string to increment.
        """
        if key in self.key_to_node:
            current_node = self.key_to_node[key]
            next_count = current_node.count + 1
            
            # Check if a bucket for the next frequency already exists
            if current_node.next.count != next_count:
                new_node = Node(next_count)
                self._add_node_after(new_node, current_node)
            
            target_node = current_node.next
            target_node.keys.add(key)
            self.key_to_node[key] = target_node
            
            # Clean up current node
            current_node.keys.remove(key)
            if not current_node.keys:
                self._remove_node(current_node)
        else:
            # Key is new, target frequency is 1
            if self.head.next.count != 1:
                new_node = Node(1)
                self._add_node_after(new_node, self.head)
            
            target_node = self.head.next
            target_node.keys.add(key)
            self.key_to_node[key] = target_node

    def dec(self, key: str) -> None:
        """
        Decrements the count of the provided key by 1.
        
        Args:
            key: The string to decrement.
        """
        if key not in self.key_to_node:
            return

        current_node = self.key_to_node[key]
        new_count = current_node.count - 1
        
        # Remove key from current bucket
        current_node.keys.remove(key)
        
        if new_count > 0:
            # Check if a bucket for the previous frequency exists
            if current_node.prev.count != new_count:
                new_node = Node(new_count)
                self._add_node_after(new_node, current_node.prev)
            
            target_node = current_node.prev
            target_node.keys.add(key)
            self.key_to_node[key] = target_node
        else:
            # Count becomes 0, remove from map
            del self.key_to_node[key]

        # Clean up current node if empty
        if not current_node.keys:
            self._remove_node(current_node)

    def getMax(self) -> str:
        """
        Returns one of the keys with the maximum frequency.
        
        Returns:
            A string key with max frequency, or empty string if none.
        """
        # The node before the tail sentinel has the highest frequency
        if self.tail.prev == self.head:
            return ""
        # Return any key from the set (O(1) via iterator)
        return next(iter(self.tail.prev.keys))

    def getMin(self) -> str:
        """
        Returns one of the keys with the minimum frequency.
        
        Returns:
            A string key with min frequency, or empty string if none.
        """
        # The node after the head sentinel has the lowest frequency
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))