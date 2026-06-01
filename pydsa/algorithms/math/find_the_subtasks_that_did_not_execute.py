METADATA = {
    "id": 1767,
    "name": "Find the Subtasks That Did Not Execute",
    "slug": "find-the-subtasks-that-did-not-execute",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["math", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Identify which subtasks (represented by bits) were not executed based on a bitmask.",
}

def solve(n: int, mask: int) -> list[int]:
    """
    Identifies the subtasks that were not executed.

    Each subtask i (from 1 to n) is represented by the (i-1)-th bit in the mask.
    If the bit is 0, the subtask was not executed.

    Args:
        n: The total number of subtasks.
        mask: A bitmask where the i-th bit represents the execution status of subtask i+1.

    Returns:
        A list of integers representing the indices of the subtasks that did not execute,
        sorted in ascending order.

    Examples:
        >>> solve(3, 5)
        [2]
        >>> solve(4, 10)
        [1, 4]
    """
    not_executed = []
    
    # Iterate through each subtask index from 1 to n
    for subtask_id in range(1, n + 1):
        # Check if the (subtask_id - 1)-th bit is set in the mask
        # We use (1 << (subtask_id - 1)) to create a bitmask for the specific subtask
        if not (mask & (1 << (subtask_id - 1))):
            not_executed.append(subtask_id)
            
    return not_executed
