METADATA = {
    "id": 1655,
    "name": "Distribute Repeating Integers",
    "slug": "distribute-repeating-integers",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Distribute integers to people such that each person gets a unique integer, maximizing the number of people who receive an integer.",
}

def solve(nums: list[int], n: int) -> int:
    """
    Distributes integers to n people such that each person receives a unique integer.
    The goal is to maximize the number of people who receive an integer.

    Args:
        nums: A list of integers available for distribution.
        n: The number of people to receive integers.

    Returns:
        The maximum number of people who can receive a unique integer.

    Examples:
        >>> solve([1, 1, 2, 2, 3, 3, 4, 4], 4)
        4
        >>> solve([1, 1, 1, 1], 4)
        1
        >>> solve([1, 2, 3, 4, 5], 3)
        3
    """
    # Sort the numbers to allow a greedy approach using a pointer
    nums.sort()
    
    count_distributed = 0
    # current_target represents the smallest integer we are currently looking to assign
    current_target = 1
    
    for num in nums:
        # If we have already satisfied all n people, we can stop
        if count_distributed == n:
            break
            
        # If the current number in the sorted list is the one we need (or larger),
        # we can assign it to the current person.
        # If num > current_target, it means we skipped some numbers, 
        # but since we want to maximize count, we just move the target up.
        if num >= current_target:
            count_distributed += 1
            # The next person must receive an integer strictly greater than the current one
            current_target = num + 1
            
    return count_distributed
