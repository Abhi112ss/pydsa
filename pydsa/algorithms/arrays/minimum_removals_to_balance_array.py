METADATA = {
    "id": 3634,
    "name": "Minimum Removals to Balance Array",
    "slug": "minimum-removals-to-balance-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "two_pointer", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of elements to remove to make the array balanced, where a balanced array has all elements of one type before all elements of another type.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of removals required to make the array balanced.
    A balanced array is defined as one where all elements of type A appear 
    before all elements of type B (for a two-type scenario).

    Args:
        nums: A list of integers representing the array.

    Returns:
        The minimum number of elements to remove to achieve a balanced state.

    Examples:
        >>> solve([1, 2, 1, 2, 1])
        2
        >>> solve([1, 1, 1])
        0
        >>> solve([2, 2, 1, 1])
        0
    """
    if not nums:
        return 0

    n = len(nums)
    
    # To make the array balanced (all 0s then all 1s, or all 1s then all 0s),
    # we want to find the longest subarray that follows the pattern [Type A... Type B...].
    # However, the problem implies a binary-like split. 
    # We can use a prefix/suffix approach or a sliding window to find the maximum 
    # number of elements we can KEEP.
    
    # Let's assume the two types are 'a' and 'b'. 
    # A balanced array looks like: [a, a, ..., a, b, b, ..., b]
    # This includes cases where only 'a' exists or only 'b' exists.
    
    # Step 1: Identify the two unique elements present in the array.
    # If there's only one type, removals = 0.
    unique_elements = list(set(nums))
    if len(unique_elements) <= 1:
        return 0
    
    type_a = unique_elements[0]
    type_b = unique_elements[1]

    def get_max_kept(first_type: int, second_type: int) -> int:
        """Finds max elements kept if first_type comes before second_type."""
        max_kept = 0
        current_kept = 0
        
        # We use a variation of the 'longest non-decreasing subsequence' logic 
        # specifically for two values.
        # count_a: max elements kept ending in type_a
        # count_ab: max elements kept ending in type_b (after some type_a)
        count_a = 0
        count_ab = 0
        
        for x in nums:
            if x == first_type:
                # If we see the first type, it can only extend a sequence of first_type
                count_a += 1
            elif x == second_type:
                # If we see the second type, it can extend a sequence of first_type 
                # OR extend a sequence that already contains second_type
                count_ab = max(count_a, count_ab) + 1
        
        return max(count_a, count_ab)

    # The result is total length minus the maximum elements we can keep 
    # in either valid configuration (A then B, or B then A).
    max_kept_config_1 = get_max_kept(type_a, type_b)
    max_kept_config_2 = get_max_kept(type_b, type_a)
    
    return n - max(max_kept_config_1, max_kept_config_2)
