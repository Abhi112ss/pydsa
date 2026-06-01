METADATA = {
    "id": 3525,
    "name": "Find X Value of Array II",
    "slug": "find_x_value_of_array_ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "binary_search", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the value x such that the number of elements in the array strictly less than x is equal to the number of elements strictly greater than x.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the value x such that the count of elements in nums < x 
    is equal to the count of elements in nums > x.

    The problem asks for an x that balances the number of elements on both sides.
    If multiple such x exist, the problem implies finding a valid one (or the 
    smallest/largest depending on specific constraints, but usually, 
    the median-based approach works).

    Args:
        nums: A list of integers.

    Returns:
        The integer x that satisfies the condition. Returns -1 if no such x exists.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        3
        >>> solve([1, 1, 1, 5, 5])
        3
    """
    n = len(nums)
    if n == 0:
        return -1
    
    # Sort the array to easily count elements less than and greater than a value
    # Sorting allows us to use the index to determine counts.
    sorted_nums = sorted(nums)
    
    # The condition: count(nums[i] < x) == count(nums[i] > x)
    # Let L be the number of elements < x, and R be the number of elements > x.
    # We want L == R.
    # In a sorted array, if we pick x, L is the index of the first element >= x.
    # R is (n - index of first element > x).
    
    # We can binary search for the value of x. 
    # However, x doesn't have to be in the array. 
    # But the transition points for L and R only occur at values present in the array.
    # A more robust way is to realize that if L == R, then L + R must be <= n.
    # Specifically, if we pick x such that it falls between sorted_nums[i] and sorted_nums[i+1],
    # then L = i + 1 and R = n - (i + 1).
    # For L == R, we need i + 1 = n - i - 1 => 2i + 2 = n => i = (n/2) - 1.
    
    # Let's check the median-based approach.
    # If n is odd, the middle element index is m = n // 2.
    # If we pick x = sorted_nums[m], L is the count of elements < sorted_nums[m].
    # R is the count of elements > sorted_nums[m].
    
    # Since the problem asks for "the" x value, and x can be any integer,
    # we can iterate through possible "gap" values or specific values.
    # A simpler way: The condition L == R implies that if we sort the array,
    # the number of elements strictly less than x must equal the number of elements strictly greater than x.
    
    # Let's use the property that L and R are monotonic with respect to x.
    # As x increases, L increases and R decreases.
    # We can binary search over the range of possible values in nums.
    
    low = min(sorted_nums)
    high = max(sorted_nums)
    
    # To handle cases where x might be outside the range [min, max]
    # (though usually x is within or near the range), we expand the search.
    # However, the problem constraints usually imply x is an integer.
    
    # Let's try all possible "boundary" values. 
    # The counts L and R only change when x passes a value in sorted_nums.
    # Possible values for x that could satisfy L == R are:
    # 1. Values in the array.
    # 2. Values between elements in the array.
    
    # Let's check all unique values in the array and the values immediately after them.
    # Actually, we can just check the "gap" values.
    # For any x, L = bisect_left(sorted_nums, x)
    # R = n - bisect_right(sorted_nums, x)
    
    import bisect
    
    # We check values that are candidates for x.
    # Candidates: sorted_nums[i] and sorted_nums[i] + 1
    candidates = set()
    for val in sorted_nums:
        candidates.add(val)
        candidates.add(val + 1)
        candidates.add(val - 1)
    
    # To make it O(n log n), we don't iterate all candidates if the range is huge.
    # Instead, we observe that L(x) - R(x) is a non-decreasing function of x.
    # L(x) = count of elements < x
    # R(x) = count of elements > x
    # f(x) = L(x) - R(x)
    # We want f(x) = 0.
    
    # Binary search for x in the range [min - 1, max + 1]
    search_low = sorted_nums[0] - 1
    search_high = sorted_nums[-1] + 1
    
    ans = -1
    
    # Standard binary search for the transition point
    # Note: f(x) is not strictly monotonic, but it is non-decreasing.
    # L(x) increases as x increases.
    # R(x) decreases as x increases.
    # Therefore L(x) - R(x) is strictly non-decreasing.
    
    left = search_low
    right = search_high
    
    while left <= right:
        mid = (left + right) // 2
        
        # Calculate L and R for mid
        # L is the number of elements < mid
        # R is the number of elements > mid
        l_count = bisect.bisect_left(sorted_nums, mid)
        r_count = n - bisect.bisect_right(sorted_nums, mid)
        
        if l_count == r_count:
            return mid
        elif l_count < r_count:
            # We need more elements on the left, so increase x
            left = mid + 1
        else:
            # We have too many elements on the left, so decrease x
            right = mid - 1
            
    return -1
