METADATA = {
    "id": 3685,
    "name": "Subsequence Sum After Capping Elements",
    "slug": "subsequence_sum_after_capping_elements",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "prefix sum", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum possible sum of a subsequence after capping all elements to a given threshold.",
}

def solve(nums: list[int], threshold: int) -> int:
    """
    Calculates the maximum sum of a subsequence where each element is capped at a threshold.
    
    The problem asks for the maximum sum of a subsequence after applying a cap. 
    Since we want to maximize the sum, we should pick all positive elements. 
    However, the problem implies we are selecting a subsequence and then applying 
    the cap to the elements chosen. To maximize the sum, we simply take every 
    element that, after being capped, contributes a positive value.
    
    Args:
        nums: A list of integers.
        threshold: The maximum value any element can take in the sum.

    Returns:
        The maximum sum of the subsequence after capping.

    Examples:
        >>> solve([1, 5, 10, 2], 5)
        13  # (min(1,5) + min(5,5) + min(10,5) + min(2,5)) = 1 + 5 + 5 + 2 = 13
        >>> solve([-1, -2, 3], 2)
        2   # (min(3,2)) = 2
    """
    # To maximize the sum, we only include elements that contribute a positive value 
    # after the cap is applied. Since the cap is applied to the element itself, 
    # an element x becomes min(x, threshold).
    # If min(x, threshold) > 0, we add it to our sum.
    
    max_sum = 0
    
    for val in nums:
        # Apply the cap to the current element
        capped_val = min(val, threshold)
        
        # If the capped value is positive, it increases our total sum
        if capped_val > 0:
            max_sum += capped_val
            
    return max_sum

# Note: The prompt mentioned sorting and prefix sums. 
# While those are useful for problems involving "k-th largest" or "subarrays",
# for a simple subsequence sum where we can pick any elements, 
# the greedy choice is to pick all elements where min(x, threshold) > 0.
# If the problem intended to limit the subsequence length to 'k', 
# then sorting and prefix sums would be required.

def solve_with_k_limit(nums: list[int], threshold: int, k: int) -> int:
    """
    An alternative interpretation: Maximize sum of a subsequence of length AT MOST k.
    This version uses the sorting and prefix sum logic suggested in the prompt.
    
    Args:
        nums: A list of integers.
        threshold: The maximum value any element can take.
        k: The maximum number of elements we can pick.

    Returns:
        The maximum sum of a subsequence of length at most k.
    """
    # 1. Transform all elements by the cap
    capped_elements = [min(x, threshold) for x in nums]
    
    # 2. Sort in descending order to pick the largest contributors
    capped_elements.sort(reverse=True)
    
    # 3. Pick the top k elements, but only if they are positive
    total_sum = 0
    for i in range(min(k, len(capped_elements))):
        if capped_elements[i] > 0:
            total_sum += capped_elements[i]
        else:
            # Since it's sorted, if this is <= 0, all subsequent are <= 0
            break
            
    return total_sum