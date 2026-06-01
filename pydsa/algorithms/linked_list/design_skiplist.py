METADATA = {
    "id": 1206,
    "name": "Design Skiplist",
    "slug": "design_skiplist",
    "category": "Design",
    "aliases": [],
    "tags": ["linked_list", "design", "randomized"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a skiplist data structure that supports search, add, and erase operations in logarithmic time.",
}

import random

class SkipListNode:
    """A node in the SkipList containing a value and a list of forward pointers."""
    def __init__(self, val: int, level: int):
        self.val = val
        # next_nodes[i] points to the next node at level i
        self.next_nodes: list[SkipListNode | None] = [None] * level

class Skiplist:
    """
    A SkipList implementation providing O(log n) average time complexity 
    for search, insertion, and deletion.
    """

    def __init__(self):
        """Initializes the skiplist with a dummy head node."""
        self.max_level = 16  # Sufficient for typical constraints
        self.p = 0.5         # Probability for level promotion
        self.head = SkipListNode(-1, self.max_level)
        self.current_max_level = 1

    def _random_level(self) -> int:
        """Generates a random level for a new node using geometric distribution."""
        lvl = 1
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        """
        Searches for a target value in the skiplist.

        Args:
            target: The integer value to search for.

        Returns:
            True if the target exists, False otherwise.

        Examples:
            >>> sl = Skiplist()
            >>> sl.add(1); sl.add(2)
            >>> sl.search(1)
            True
            >>> sl.search(3)
            False
        """
        current = self.head
        # Traverse from the highest level down to level 0
        for i in range(self.current_max_level - 1, -1, -1):
            while current.next_nodes[i] and current.next_nodes[i].val < target:
                current = current.next_nodes[i]
        
        # Move to the potential node at level 0
        current = current.next_nodes[0]
        return current is not None and current.val == target

    def add(self, val: int) -> None:
        """
        Adds a value to the skiplist.

        Args:
            val: The integer value to add.
        """
        # update_nodes stores the rightmost node at each level that is less than val
        update_nodes: list[SkipListNode] = [None] * self.max_level
        current = self.head
        
        for i in range(self.current_max_level - 1, -1, -1):
            while current.next_nodes[i] and current.next_nodes[i].val < val:
                current = current.next_nodes[i]
            update_nodes[i] = current

        new_level = self._random_level()
        if new_level > self.current_max_level:
            # If new level exceeds current max, update the head pointers for new levels
            for i in range(self.current_max_level, new_level):
                update_nodes[i] = self.head
            self.current_max_level = new_level

        new_node = SkipListNode(val, new_level)
        # Insert the new node by updating pointers at each level
        for i in range(new_level):
            new_node.next_nodes[i] = update_nodes[i].next_nodes[i]
            update_nodes[i].next_nodes[i] = new_node

    def erase(self, val: int) -> bool:
        """
        Removes a value from the skiplist if it exists.

        Args:
            val: The integer value to remove.

        Returns:
            True if the value was found and removed, False otherwise.
        """
        update_nodes: list[SkipListNode] = [None] * self.max_level
        current = self.head

        # Find the nodes preceding the target at each level
        for i in range(self.current_max_level - 1, -1, -1):
            while current.next_nodes[i] and current.next_nodes[i].val < val:
                current = current.next_nodes[i]
            update_nodes[i] = current

        # The target node must be the immediate next node at level 0
        target_node = current.next_nodes[0]

        if not target_node or target_node.val != val:
            return False

        # Remove the node by bypassing it at all levels where it exists
        for i in range(self.current_max_level):
            if update_nodes[i].next_nodes[i] != target_node:
                break
            update_nodes[i].next_nodes[i] = target_node.next_nodes[i]

        # Shrink current_max_level if top levels are now empty
        while self.current_max_level > 1 and self.head.next_nodes[self.current_max_level - 1] is None:
            self.current_max_level -= 1
            
        return True

def solve():
    """Entry point for testing the Skiplist implementation."""
    sl = Skiplist()
    sl.add(1)
    sl.add(2)
    sl.add(3)
    print(f"Search 1: {sl.search(1)}")  # Expected: True
    print(f"Search 4: {sl.search(4)}")  # Expected: False
    print(f"Erase 1: {sl.erase(1)}")    # Expected: True
    print(f"Search 1: {sl.search(1)}")  # Expected: False
    print(f"Erase 1: {sl.erase(1)}")    # Expected: False
