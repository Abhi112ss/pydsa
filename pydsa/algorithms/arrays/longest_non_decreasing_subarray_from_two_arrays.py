METADATA = {
    "id": 2771,
    "name": "Longest Non-decreasing Subarray From Two Arrays",
    "slug": "longest-non-decreasing-subarray-from-two-arrays",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "two_pointer", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subarray such that the combined elements from two arrays form a non-decreasing sequence.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Finds the length of the longest non-decreasing subarray formed by 
    interleaving elements from nums1 and nums2 at the same index.

    Args:
        nums1: The first array of integers.
        nums2: The second array of integers.

    Returns:
        The length of the longest non-decreasing subarray.

    Examples:
        >>> solve([1, 2, 3], [1, 2, 3])
        3
        >>> solve([1, 5, 3], [2, 4, 6])
        2
        >>> solve([1, 1, 1], [1, 1, 1])
        3
    """
    n = len(nums1)
    if n == 0:
        return 0

    max_length = 0
    current_length = 0
    previous_value = float('-inf')

    for i in range(n):
        # We have two choices at each index i: 
        # 1. Pick nums1[i] if it is >= previous_value
        # 2. Pick nums2[i] if it is >= previous_value
        
        # To maximize the length, we want to pick the smallest possible 
        # value that is still >= previous_value to leave more room 
        # for future elements.
        
        val1 = nums1[i]
        val2 = nums2[i]
        
        # Determine the smallest valid choice at the current index
        best_choice = float('inf')
        
        # Check if nums1[i] can extend the sequence
        if val1 >= previous_value:
            best_choice = min(best_choice, val1)
            
        # Check if nums2[i] can extend the sequence
        if val2 >= previous_value:
            best_choice = min(best_choice, val2)

        if best_choice != float('inf'):
            # If we found a valid element, increment current sequence length
            current_length += 1
            previous_value = best_choice
        else:
            # If neither element can extend the sequence, we must restart.
            # The new sequence starts with the smaller of the two current elements.
            current_length = 1
            previous_value = min(val1, val2)
            
        max_length = max(max_length, current_length)

    return max_length
