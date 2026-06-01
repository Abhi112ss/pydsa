METADATA = {
    "id": 1588,
    "name": "Sum of All Odd Length Subarrays",
    "slug": "sum-of-all-odd-length-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["math", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of all possible odd-length subarrays of a given array.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the sum of all odd-length subarrays using a combinatorial approach.

    For each element at index i, we calculate how many odd-length subarrays 
    contain it. An element at index i is part of a subarray starting at index 'left' 
    and ending at index 'right' if 0 <= left <= i <= right < n.

    Args:
        arr: A list of integers.

    Returns:
        The sum of all odd-length subarrays.

    Examples:
        >>> solve([1, 4, 2, 5, 3])
        58
        >>> solve([1, 2, 3])
        10
    """
    total_sum = 0
    n = len(arr)

    for i in range(n):
        # Number of choices for the start of the subarray (0 to i)
        choices_left = i + 1
        # Number of choices for the end of the subarray (i to n-1)
        choices_right = n - i
        
        # Total number of subarrays containing arr[i] is choices_left * choices_right.
        # In any set of consecutive integers, roughly half are odd and half are even.
        # Specifically, for a range of total subarrays, the number of odd-length 
        # subarrays is ceil(total_subarrays / 2).
        total_subarrays = choices_left * choices_right
        odd_subarrays_count = (total_subarrays + 1) // 2
        
        total_sum += odd_subarrays_count * arr[i]

    return total_sum
