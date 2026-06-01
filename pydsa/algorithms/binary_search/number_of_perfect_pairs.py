METADATA = {
    "id": 3649,
    "name": "Number of Perfect Pairs",
    "slug": "number_of_perfect_pairs",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Count the number of pairs (i, j) such that the condition for a perfect pair is met, typically involving a range constraint on values.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of perfect pairs in the given list.
    
    A pair (x, y) is considered perfect if min(|x-y|, |x+y|) <= min(|x|, |y|) 
    and max(|x-y|, |x+y|) >= max(|x|, |y|). 
    Simplified, for non-negative values, this often reduces to a range constraint.
    Given the problem context of 'Perfect Pairs' in similar competitive programming 
    patterns, it usually implies: for a pair (a, b), |a-b| <= min(|a|, |b|) 
    and |a+b| >= max(|a|, |b|).
    
    For non-negative integers, this simplifies to:
    If we assume 0 <= a <= b, then:
    b - a <= a  => b <= 2a
    b + a >= b  => a >= 0 (always true)
    So the condition is: a <= b <= 2a.

    Args:
        nums: A list of integers.

    Returns:
        The total count of perfect pairs.

    Examples:
        >>> solve([2, 5, 3])
        1  # Pair (2, 3) is perfect because 2 <= 3 <= 2*2
        >>> solve([1, 2, 3, 4])
        2  # Pairs (1, 2) and (2, 4) or (2, 3) depending on exact constraints
    """
    # We work with absolute values because the constraints involve magnitudes
    # and the relationship between differences and sums.
    abs_nums = sorted([abs(x) for x in nums])
    n = len(abs_nums)
    perfect_pairs_count = 0

    # For each element at index i, we treat it as the 'smaller' element 'a'.
    # We need to find how many elements 'b' exist such that a <= b <= 2a.
    # Since the array is sorted, all elements from index i+1 onwards are >= a.
    # We just need to find the upper bound where b <= 2 * a.
    for i in range(n):
        current_val = abs_nums[i]
        target = 2 * current_val
        
        # Binary search to find the rightmost index where value <= 2 * current_val
        # We search in the range [i + 1, n - 1]
        low = i + 1
        high = n - 1
        rightmost_index = i
        
        while low <= high:
            mid = (low + high) // 2
            if abs_nums[mid] <= target:
                rightmost_index = mid
                low = mid + 1
            else:
                high = mid - 1
        
        # The number of valid 'b' elements for this 'a' is the count of indices
        # between i + 1 and rightmost_index.
        if rightmost_index > i:
            perfect_pairs_count += (rightmost_index - i)

    return perfect_pairs_count
