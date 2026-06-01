METADATA = {
    "id": 3379,
    "name": "Transformed Array",
    "slug": "transformed-array",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Transform an array based on the count of elements strictly less than the current element.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Transforms the input array based on the count of elements strictly less than each element.

    The transformation rule:
    For each index i, the new value is the count of elements in the original array 
    that are strictly less than nums[i].

    Args:
        nums: A list of integers representing the original array.

    Returns:
        A list of integers representing the transformed array.

    Examples:
        >>> solve([0, 1, 2, 3])
        [0, 1, 2, 3]
        >>> solve([1, 1, 1, 1])
        [0, 0, 0, 0]
        >>> solve([2, 1, 3, 1, 2])
        [2, 0, 4, 0, 2]
    """
    n = len(nums)
    if n == 0:
        return []

    # Step 1: Count the frequency of each number using a frequency map
    # This allows us to handle duplicates efficiently.
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Step 2: Sort the unique keys to calculate prefix sums
    # The number of elements strictly less than x is the sum of frequencies 
    # of all elements smaller than x.
    sorted_unique_elements = sorted(counts.keys())
    
    # Map each unique element to the count of elements strictly less than it
    less_than_count_map = {}
    running_sum = 0
    for element in sorted_unique_elements:
        less_than_count_map[element] = running_sum
        running_sum += counts[element]

    # Step 3: Construct the result array using the precomputed map
    result = []
    for num in nums:
        result.append(less_than_count_map[num])

    return result
