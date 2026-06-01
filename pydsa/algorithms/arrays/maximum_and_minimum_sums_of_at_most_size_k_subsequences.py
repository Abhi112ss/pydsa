METADATA = {
    "id": 3428,
    "name": "Maximum and Minimum Sums of at Most Size K Subsequences",
    "slug": "maximum_and_minimum_sums_of_at_most_size_k_subsequences",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum and minimum possible sums of a subsequence with length at most K.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Calculates the maximum and minimum sums of a subsequence of length at most K.

    To maximize the sum, we should pick the largest positive numbers available, 
    up to K elements. If there are fewer than K positive numbers, we pick all 
    positive numbers. If all numbers are negative, the maximum sum of a 
    subsequence of length at most K is 0 (by picking an empty subsequence).
    
    To minimize the sum, we should pick the smallest negative numbers available, 
    up to K elements. If there are fewer than K negative numbers, we pick all 
    negative numbers. If all numbers are positive, the minimum sum of a 
    subsequence of length at most K is 0 (by picking an empty subsequence).

    Args:
        nums: A list of integers.
        k: The maximum allowed size of the subsequence.

    Returns:
        A list containing two integers: [maximum_sum, minimum_sum].

    Examples:
        >>> solve([1, -2, 3, -4, 5], 2)
        [8, -6]
        >>> solve([-1, -2, -3], 2)
        [0, -5]
        >>> solve([1, 2, 3], 2)
        [5, 0]
    """
    # To maximize sum: pick up to K largest positive elements.
    # To minimize sum: pick up to K smallest negative elements.
    
    # Sort the array to easily access largest and smallest elements
    sorted_nums = sorted(nums)
    n = len(nums)
    
    # Calculate Maximum Sum
    # We want the largest elements, but only if they are > 0.
    # We can take at most k elements.
    max_sum = 0
    count_max = 0
    # Iterate from the end of the sorted array (largest elements)
    for i in range(n - 1, -1, -1):
        if count_max < k and sorted_nums[i] > 0:
            max_sum += sorted_nums[i]
            count_max += 1
        else:
            break
            
    # Calculate Minimum Sum
    # We want the smallest elements, but only if they are < 0.
    # We can take at most k elements.
    min_sum = 0
    count_min = 0
    # Iterate from the start of the sorted array (smallest elements)
    for i in range(n):
        if count_min < k and sorted_nums[i] < 0:
            min_sum += sorted_nums[i]
            count_min += 1
        else:
            break
            
    return [max_sum, min_sum]
