METADATA = {
    "id": 2680,
    "name": "Maximum OR",
    "slug": "maximum-or",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy", "prefix-suffix"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible value of the bitwise OR of elements in an array after performing exactly n-1 operations where each operation shifts an element to the left by one bit.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum possible bitwise OR value by shifting elements.

    The problem asks us to maximize the OR sum of an array after performing 
    n-1 operations. Each operation consists of picking an element and 
    shifting it left by 1. Effectively, we can distribute the total number 
    of shifts (n-1) among the elements. However, the optimal strategy is 
    to apply all shifts to a single element to push its bits to the highest 
    possible positions.

    Args:
        nums: A list of integers.

    Returns:
        The maximum bitwise OR value possible.

    Examples:
        >>> solve([8, 1, 2])
        34
        >>> solve([4, 2])
        8
    """
    n = len(nums)
    if n == 0:
        return 0

    # Precompute prefix and suffix ORs to efficiently calculate 
    # the OR sum of all elements except the one being shifted.
    prefix_ors = [0] * (n + 1)
    suffix_ors = [0] * (n + 1)

    for i in range(n):
        prefix_ors[i + 1] = prefix_ors[i] | nums[i]

    for i in range(n - 1, -1, -1):
        suffix_ors[i] = suffix_ors[i + 1] | nums[i]

    max_or_sum = 0

    # Iterate through each number, assuming it is the one receiving 
    # all (n-1) shifts. The total OR sum for index i will be:
    # (prefix_or up to i-1) | (nums[i] << (n-1)) | (suffix_or from i+1)
    for i in range(n):
        # Calculate the OR sum of all elements excluding nums[i]
        others_or = prefix_ors[i] | suffix_ors[i + 1]
        
        # Shift the current element by the total available shifts (n-1)
        # and combine it with the OR sum of all other elements.
        current_total_or = others_or | (nums[i] << (n - 1))
        
        if current_total_or > max_or_sum:
            max_or_sum = current_total_or

    return max_or_sum
