METADATA = {
    "id": 1296,
    "name": "Divide Array in Sets of K Consecutive Numbers",
    "slug": "divide-array-in-sets-of-k-consecutive-numbers",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be divided into sets of k consecutive numbers.",
}

def solve(nums: list[int], k: int) -> bool:
    """
    Determines if the array can be divided into sets of k consecutive numbers.

    Args:
        nums: A list of integers.
        k: The required size of each consecutive sequence.

    Returns:
        True if the array can be partitioned into sets of k consecutive numbers, 
        False otherwise.

    Examples:
        >>> solve([1, 2, 3, 3, 4, 4, 5, 6], 4)
        True
        >>> solve([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3)
        True
        >>> solve([3, 3, 6, 4, 7, 10], 3)
        False
    """
    # If the total elements are not divisible by k, it's impossible
    if len(nums) % k != 0:
        return False

    # Count the frequency of each number
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Sort the unique numbers to process them greedily from smallest to largest
    sorted_keys = sorted(frequency_map.keys())

    for num in sorted_keys:
        count = frequency_map[num]
        
        # If this number has already been used up by previous sequences
        if count > 0:
            # This number must be the start of 'count' number of sequences
            # because it is the smallest available number.
            # Therefore, the next k-1 consecutive numbers must also exist 
            # at least 'count' times.
            for i in range(num, num + k):
                if frequency_map.get(i, 0) < count:
                    return False
                frequency_map[i] -= count

    return True
