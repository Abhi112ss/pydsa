METADATA = {
    "id": 2465,
    "name": "Number of Distinct Averages",
    "slug": "number-of-distinct-averages",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "hash_set", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the number of distinct averages formed by pairing the smallest and largest elements of a sorted array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of distinct averages formed by pairing the smallest 
    and largest elements of the given array.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The count of unique averages.

    Examples:
        >>> solve([2, 3, 5, 8])
        2
        >>> solve([1, 1, 1, 1])
        1
    """
    # Sorting is required to pair the smallest with the largest efficiently.
    # While the prompt suggests O(n) expected, sorting makes it O(n log n).
    # If the input were guaranteed sorted, it would be O(n).
    nums.sort()
    
    distinct_sums = set()
    left_index = 0
    right_index = len(nums) - 1
    
    # Use two pointers to move from both ends towards the center.
    while left_index < right_index:
        # We store the sum instead of the average (sum/2) to avoid 
        # floating point precision issues. If sums are unique, averages are unique.
        current_sum = nums[left_index] + nums[right_index]
        distinct_sums.add(current_sum)
        
        left_index += 1
        right_index -= 1
        
    return len(distinct_sums)
