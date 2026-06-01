METADATA = {
    "id": 3678,
    "name": "Smallest Absent Positive Greater Than Average",
    "slug": "smallest-absent-positive-greater-than-average",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "math", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest positive integer greater than the average of the array that is not present in the array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the smallest positive integer greater than the average of the input array 
    that does not exist in the array.

    Args:
        nums: A list of integers.

    Returns:
        The smallest positive integer > average(nums) that is not in nums.

    Examples:
        >>> solve([1, 2, 3])
        4
        >>> solve([1, 10, 5])
        6
        >>> solve([-1, -2, -3])
        1
    """
    if not nums:
        return 1

    # Calculate the average of the array
    total_sum = sum(nums)
    average = total_sum / len(nums)

    # Convert list to a set for O(1) average-case lookup
    presence_set = set(nums)

    # Start checking from the smallest possible positive integer 
    # that is strictly greater than the average.
    # If average is 2.5, start at 3. If average is -5, start at 1.
    current_candidate = max(1, int(average // 1) + 1)
    
    # If the floor-based calculation doesn't strictly exceed the average 
    # (e.g., average is 3.0, current_candidate becomes 3), increment it.
    if current_candidate <= average:
        current_candidate += 1

    # Iterate upwards until we find a number not in the set
    while current_candidate in presence_set:
        current_candidate += 1

    return current_candidate
