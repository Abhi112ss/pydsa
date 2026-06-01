METADATA = {
    "id": 3584,
    "name": "Maximum Product of First and Last Elements of a Subsequence",
    "slug": "maximum-product-of-first-and-last-elements-of-a-subsequence",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum product of the first and last elements of any non-empty subsequence of the given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum product of the first and last elements of any subsequence.
    
    A subsequence is formed by deleting zero or more elements from the original array.
    The first and last elements of a subsequence are simply two elements from the 
    original array where the index of the first is less than or equal to the index 
    of the last.
    
    Note: If the subsequence has only one element, the first and last elements 
    are the same element.

    Args:
        nums: A list of integers.

    Returns:
        The maximum possible product of the first and last elements of a subsequence.

    Examples:
        >>> solve([1, 2, 3, 4])
        16
        >>> solve([-1, -2, -3, -4])
        16
        >>> solve([-1, 5, -2])
        25
        >>> solve([0, -5, 0])
        0
    """
    if not nums:
        return 0

    # The problem asks for the max product of nums[i] * nums[j] where i <= j.
    # Case 1: i == j. The product is nums[i]^2.
    # Case 2: i < j. The product is nums[i] * nums[j].
    
    # To maximize nums[i] * nums[j]:
    # - If we pick two positive numbers, we want the two largest possible.
    # - If we pick two negative numbers, we want the two smallest (most negative) possible.
    # - If we pick one positive and one negative, we want the smallest absolute product.
    # - If we pick a single element, we want the largest square.

    # However, the constraint is i <= j. 
    # For any pair (i, j) with i < j, we can always pick them as first and last.
    # For any single element i, we can pick it as both first and last.
    
    # Therefore, the problem reduces to finding max(nums[i] * nums[j]) for all i <= j.
    # This is equivalent to finding the max of:
    # 1. The square of any element (covers i == j).
    # 2. The product of any two distinct elements (covers i < j).
    
    # To find the max product of any two elements (i < j):
    # - Max positive * Max positive
    # - Min negative * Min negative
    # - Max positive * Min negative (only if all products are negative)

    max_val = float('-inf')
    min_val = float('inf')
    max_sq = 0
    
    # We need to track the two largest and two smallest to handle all sign combinations
    # but since we can pick i == j, we just need to find the global max/min 
    # and the max square.
    
    # Actually, the simplest way to cover all i <= j:
    # The max product is either:
    # - The square of the element with the largest absolute value.
    # - The product of the two largest elements (if they are positive).
    # - The product of the two smallest elements (if they are negative).
    # - The product of the largest and smallest (if one is positive and one is negative).
    
    # Let's find the four candidates:
    # 1. max(x^2) for all x in nums
    # 2. max(x * y) for all x, y in nums where index(x) < index(y)
    
    # To find max(x * y) for i < j:
    # We can track the running min and max seen so far to find the best product.
    # But since we can pick any i < j, we just need the two largest and two smallest.
    
    # Let's refine:
    # The maximum product of ANY two elements (i != j) is:
    # max(largest * second_largest, smallest * second_smallest)
    # The maximum product of ANY single element (i == j) is:
    # max(x * x)
    
    # Because the problem allows i <= j, we just need to check:
    # 1. All x*x
    # 2. All x*y where i < j
    
    # Let's find the two largest and two smallest values in the array.
    # We also need to handle the case where the array has only one element.
    
    if len(nums) == 1:
        return nums[0] * nums[0]

    # Find the two largest and two smallest values
    # We use sorting for simplicity, O(N log N) is acceptable if N is reasonable,
    # but the prompt asks for O(N).
    
    first_max = float('-inf')
    second_max = float('-inf')
    first_min = float('inf')
    second_min = float('inf')
    max_single_sq = 0

    for x in nums:
        # Update max single square
        max_single_sq = max(max_single_sq, x * x)
        
        # Update two largest
        if x > first_max:
            second_max = first_max
            first_max = x
        elif x > second_max:
            second_max = x
            
        # Update two smallest
        if x < first_min:
            second_min = first_min
            first_min = x
        elif x < second_min:
            second_min = x

    # Candidates for max product:
    # 1. The largest square (i == j)
    # 2. Product of two largest (i < j, both positive)
    # 3. Product of two smallest (i < j, both negative)
    # 4. Product of largest and smallest (i < j, one pos, one neg)
    
    candidates = [max_single_sq]
    
    # If we have at least two elements, we can pick i < j
    # We check the products of the extremes
    candidates.append(first_max * second_max)
    candidates.append(first_min * second_min)
    candidates.append(first_max * first_min)
    
    return int(max(candidates))
