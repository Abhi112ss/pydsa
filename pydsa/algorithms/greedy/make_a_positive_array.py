METADATA = {
    "id": 3511,
    "name": "Make a Positive Array",
    "slug": "make_a_positive_array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Transform an array into one where all elements are positive by flipping signs of elements using a limited number of operations.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Transforms the input array such that as many elements as possible are positive,
    using at most k sign-flip operations.

    The strategy is to greedily flip the most negative numbers first to maximize
    the number of positive elements and the total sum.

    Args:
        nums: A list of integers.
        k: The maximum number of sign-flip operations allowed.

    Returns:
        A list of integers representing the transformed array.

    Examples:
        >>> solve([-4, -2, 0, 3, 5], 2)
        [4, 2, 0, 3, 5]
        >>> solve([-1, -1, -1], 1)
        [1, -1, -1]
    """
    # Sort the array to bring the most negative numbers to the front
    nums.sort()
    
    n = len(nums)
    index = 0
    
    # Step 1: Greedily flip negative numbers to positive
    while index < n and k > 0 and nums[index] < 0:
        nums[index] = -nums[index]
        index += 1
        k -= 1
        
    # Step 2: If we still have flips left and the current element is 0,
    # we can use all remaining flips on 0 without changing the array.
    if index < n and nums[index] == 0:
        return nums
        
    # Step 3: If we still have flips left and they are odd, 
    # we must flip the smallest absolute value to minimize the impact.
    # Since the array was sorted and we flipped negatives, the smallest 
    # absolute value is either at 'index' or 'index - 1'.
    # However, because we want to handle the remaining k efficiently, 
    # if k is odd, we flip the element at the current index (which is the 
    # smallest non-negative element) or the last flipped element.
    # A simpler way: if k is odd, flip the smallest element in the current state.
    if k % 2 == 1:
        # Re-sort or find min to handle the case where a previously negative 
        # number is now smaller than the next positive number.
        # But since we only care about the parity of k, we just find the minimum.
        min_val_idx = 0
        min_val = nums[0]
        for i in range(1, n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_val_idx = i
        nums[min_val_idx] = -nums[min_val_idx]
        
    return nums
