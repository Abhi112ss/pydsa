METADATA = {
    "id": 234,
    "name": "Palindrome Linked List",
    "slug": "palindrome_linked_list",
    "category": "Linked List",
    "aliases": ["is_palindrome_linked_list"],
    "tags": ["linked_list", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a singly linked list is a palindrome by reversing the second half and comparing with the first half.",
}


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head: ListNode | None) -> bool:
    """Check if a singly linked list is a palindrome.

    Uses O(1) extra space by reversing the second half of the list in-place,
    then comparing node values of the first half against the reversed second half.

    Args:
        head: The head node of the singly linked list.

    Returns:
        True if the linked list is a palindrome, False otherwise.

    Examples:
        >>> solve(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        True
        >>> solve(ListNode(1, ListNode(2)))
        False
    """
    if not head or not head.next:
        return True

    # Step 1: Use slow/fast pointers to find the middle of the list.
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list starting from 'slow'.
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    # 'prev' is now the head of the reversed second half.

    # Step 3: Compare the first half with the reversed second half.
    first_half = head
    second_half = prev
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True