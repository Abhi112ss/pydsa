METADATA = {
    "id": 2918,
    "name": "Minimum Equal Sum of Two Arrays After Replacing Zeros",
    "slug": "minimum-equal-sum-of-two-arrays-after-replacing-zeros",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum possible equal sum of two arrays after replacing all zeros with positive integers.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum possible equal sum of two arrays after replacing 
    all zeros with positive integers.

    Args:
        nums1: The first array of integers.
        nums2: The second array of integers.

    Returns:
        The minimum equal sum if possible, otherwise -1.

    Examples:
        >>> solve([1, 2, 3, 0], [2, 1, 3, 4])
        11
        >>> solve([1, 1, 1, 1], [1, 1, 1, 1])
        4
        >>> solve([1, 0, 1], [2, 0, 2])
        -1
    """
    sum1 = 0
    zeros1 = 0
    for num in nums1:
        if num == 0:
            zeros1 += 1
        else:
            sum1 += num

    sum2 = 0
    zeros2 = 0
    for num in nums2:
        if num == 0:
            zeros2 += 1
        else:
            sum2 += num

    # The minimum possible sum for an array is its current sum 
    # plus the number of zeros (since each zero must be at least 1).
    min_possible_sum1 = sum1 + zeros1
    min_possible_sum2 = sum2 + zeros2

    # Case 1: Both arrays have no zeros. They must be exactly equal.
    if zeros1 == 0 and zeros2 == 0:
        return sum1 if sum1 == sum2 else -1

    # Case 2: One array has zeros, the other doesn't.
    # The array with zeros can increase its sum to any value >= min_possible_sum.
    # The array without zeros must be >= its current sum.
    if zeros1 > 0 and zeros2 == 0:
        return sum2 if sum2 >= min_possible_sum1 else -1
    
    if zeros2 > 0 and zeros1 == 0:
        return sum1 if sum1 >= min_possible_sum2 else -1

    # Case 3: Both arrays have at least one zero.
    # We can always make the sums equal to the maximum of the two minimum possible sums.
    return max(min_possible_sum1, min_possible_sum2)
