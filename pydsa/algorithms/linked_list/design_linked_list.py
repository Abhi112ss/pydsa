METADATA = {
    "id": 707,
    "name": "Design Linked List",
    "slug": "design-linked-list",
    "category": "Design",
    "aliases": [],
    "tags": ["linked_list", "design"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Implement a Singly Linked List with get, addAtHead, addAtTail, addAtIndex, and deleteAtIndex methods.",
}

class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val: int = 0, next_node: 'ListNode' = None):
        self.val = val
        self.next = next_node

class MyLinkedList:
    """
    A singly linked list implementation.
    
    Attributes:
        size (int): The number of elements currently in the list.
        head (ListNode): A dummy head node to simplify edge cases.
    """

    def __init__(self) -> None:
        """Initializes the linked list with a dummy head."""
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        """
        Returns the value of the index-th node in the linked list. 
        If the index is invalid, returns -1.

        Args:
            index (int): The zero-based index of the node to retrieve.

        Returns:
            int: The value of the node at the given index, or -1 if invalid.

        Examples:
            >>> l = MyLinkedList()
            >>> l.addAtTail(1)
            >>> l.get(0)
            1
            >>> l.get(1)
            -1
        """
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Adds a node with the specified value at the head of the list.

        Args:
            val (int): The value to be added.
        """
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Appends a node with the specified value to the end of the list.

        Args:
            val (int): The value to be added.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Adds a node with the specified value at the index. 
        If index equals the length of the list, the node will be appended to the end. 
        If index is greater than the length, the node will not be inserted.
        If index is negative, it is treated as 0.

        Args:
            index (int): The index at which to insert the node.
            val (int): The value to be added.

        Examples:
            >>> l = MyLinkedList()
            >>> l.addAtHead(1)
            >>> l.addAtTail(3)
            >>> l.addAtIndex(1, 2)
            >>> l.get(1)
            2
        """
        if index > self.size:
            return
        
        index = max(0, index)
        
        # Traverse to the node immediately preceding the insertion point
        prev = self.head
        for _ in range(index):
            prev = prev.next
            
        new_node = ListNode(val, prev.next)
        prev.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Deletes the index-th node in the linked list, if the index is valid.

        Args:
            index (int): The zero-based index of the node to be deleted.

        Examples:
            >>> l = MyLinkedList()
            >>> l.addAtHead(1)
            >>> l.addAtTail(3)
            >>> l.deleteAtIndex(0)
            >>> l.get(0)
            3
        """
        if index < 0 or index >= self.size:
            return

        # Traverse to the node immediately preceding the node to be deleted
        prev = self.head
        for _ in range(index):
            prev = prev.next
            
        # Bypass the target node to remove it from the chain
        prev.next = prev.next.next
        self.size -= 1

def solve():
    """
    Entry point for testing the MyLinkedList implementation.
    """
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3
    linked_list.deleteAtIndex(1)
    assert linked_list.get(1) == 3
    print("All tests passed!")
