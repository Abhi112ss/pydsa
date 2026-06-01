METADATA = {
    "id": 148,
    "name": "Sort List",
    "slug": "sort-list",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "merge_sort", "divide_and_conquer"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(log n)",
    "description": "Sort a linked list in O(n log n) time and O(1) space (or O(log n) due to recursion stack).",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Sorts a singly-linked list using the Merge Sort algorithm.

    Args:
        head: The head of the singly-linked list to be sorted.

    Returns:
        The head of the sorted singly-linked list.

    Examples:
        >>> head = ListNode(4, ListNode(2, ListNode(1, ListNode(3)))
        >>> sorted_head = solve(head)
        >>> # sorted_head represents 1 -> 2 -> 3 -> 4
    """
    if not head or not head.next:
        return head

    # Step 1: Split the list into two halves using slow and fast pointers
    mid = get_middle(head)
    left_half = head
    right_half = mid.next
    mid.next = None  # Break the link to create two separate lists

    # Step 2: Recursively sort both halves
    left_sorted = solve(left_half)
    right_sorted = solve(right_half)

    # Step 3: Merge the two sorted halves
    return merge(left_sorted, right_sorted)

def get_middle(head: ListNode) -> ListNode:
    """
    Finds the middle node of the linked list using the tortoise and hare approach.
    
    Args:
        head: The head of the list.
        
    Returns:
        The node representing the end of the first half.
    """
    slow = head
    fast = head.next  # Start fast one step ahead to get the end of the first half

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    Merges two sorted linked lists into one sorted linked list.

    Args:
        list1: Head of the first sorted list.
        list2: Head of the second sorted list.

    Returns:
        Head of the merged sorted list.
    """
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining nodes from whichever list is not empty
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next