METADATA = {
    "id": 3782,
    "name": "Last Remaining Integer After Alternating Deletion Operations",
    "slug": "last-remaining-integer-after-alternating-deletion-operations",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation", "sequence"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the last remaining integer in a sequence from 1 to n after repeatedly removing elements in alternating patterns.",
}

def solve(n: int) -> int:
    """
    Finds the last remaining integer after alternating deletion operations.
    
    The process starts with a sequence [1, 2, ..., n]. 
    In each step, we remove elements based on a specific pattern (e.g., every 
    k-th element or alternating directions). This implementation follows the 
    mathematical pattern of tracking the head of the sequence and the step size.

    Args:
        n: The upper bound of the initial sequence [1, ..., n].

    Returns:
        The last remaining integer in the sequence.

    Examples:
        >>> solve(10)
        4
        >>> solve(1)
        1
    """
    if n <= 0:
        return 0
    
    # head: the first element of the current sequence
    # step: the distance between elements in the current sequence
    # remaining: how many elements are left in the sequence
    # left_to_right: boolean to track the direction of deletion
    head = 1
    step = 1
    remaining = n
    left_to_right = True

    while remaining > 1:
        # In the first pass (left to right), the head is always removed.
        # In subsequent passes (right to left), the head is only removed 
        # if the number of elements is odd or if we are moving left to right.
        # For this specific problem logic (alternating deletions):
        if left_to_right or (remaining % 2 == 1):
            head += step
        
        # After each pass, the number of elements is halved
        remaining //= 2
        # The distance between remaining elements doubles
        step *= 2
        # Flip the direction for the next pass
        left_to_right = not left_to_right

    return head
