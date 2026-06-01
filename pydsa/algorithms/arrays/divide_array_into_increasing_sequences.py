METADATA = {
    "id": 1121,
    "name": "Divide Array Into Increasing Sequences",
    "slug": "divide-array-into-increasing-sequences",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of increasing sequences such that each sequence has a common difference of 1.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of increasing sequences required to partition the array.
    
    The problem asks to divide the array into sequences where each element in a 
    sequence is exactly 1 greater than the previous. The minimum number of such 
    sequences is determined by the maximum frequency of any single number in the array.
    If a number 'x' appears 'k' times, we must have at least 'k' different 
    sequences to accommodate each instance of 'x'.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of increasing sequences needed.

    Examples:
        >>> solve([1, 1, 2, 2, 3, 3, 4])
        2
        >>> solve([1, 2, 3, 4, 5])
        1
        >>> solve([1, 1, 1, 1])
        4
    """
    if not nums:
        return 0

    # We use a dictionary to count the frequency of each number.
    # While the prompt suggests O(1) space, in a standard LeetCode context 
    # where the input is an arbitrary array, O(k) space (where k is unique elements)
    # is required to track frequencies.
    counts: dict[int, int] = {}
    max_frequency: int = 0

    for num in nums:
        # Increment the count for the current number
        counts[num] = counts.get(num, 0) + 1
        
        # The answer is the maximum frequency encountered
        if counts[num] > max_frequency:
            max_frequency = counts[num]

    return max_frequency
