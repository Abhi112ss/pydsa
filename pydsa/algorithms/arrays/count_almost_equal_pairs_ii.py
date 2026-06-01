METADATA = {
    "id": 3267,
    "name": "Count Almost Equal Pairs II",
    "slug": "count-almost-equal-pairs-ii",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs of indices (i, j) such that i < j and nums[i] and nums[j] are almost equal, meaning they are equal or can be made equal by swapping exactly one pair of elements.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of pairs (i, j) with i < j such that nums[i] and nums[j] 
    are 'almost equal'. Two numbers are almost equal if they are equal or 
    if swapping one element in one makes them equal.
    
    Note: In the context of single integers, 'almost equal' usually implies 
    the values themselves are equal or satisfy a specific property. 
    Based on the problem constraints for 'Almost Equal Pairs II' (often 
    referring to digit swaps or specific value properties), this implementation 
    handles the case where 'almost equal' means the numbers are equal or 
    can be made equal by swapping digits.

    Args:
        nums: A list of integers.

    Returns:
        The total count of almost equal pairs.

    Examples:
        >>> solve([1, 1, 2])
        1
        >>> solve([12, 21, 12])
        3
    """
    from collections import Counter

    def get_canonical_form(n: int) -> tuple[int, ...]:
        """
        Returns a sorted tuple of digits to represent the 'equivalence class' 
        of a number under digit swapping.
        """
        return tuple(sorted(list(str(n))))

    # To count pairs (i, j) where nums[i] and nums[j] are almost equal:
    # 1. They are identical.
    # 2. They are permutations of each other (e.g., 12 and 21).
    
    # However, the standard definition for 'Almost Equal' in these problems 
    # often distinguishes between 'equal' and 'swappable'.
    # If the problem implies nums[i] == nums[j] OR nums[i] is a permutation of nums[j]:
    
    # We use a frequency map to count occurrences of each number.
    # We also use a frequency map for the 'sorted digit' representation.
    
    exact_counts = Counter()
    permutation_counts = Counter()
    total_pairs = 0

    for num in nums:
        # The canonical form represents the number's digits sorted.
        # Any number with the same canonical form can be made equal via swaps.
        canonical = get_canonical_form(num)
        
        # 1. Add pairs where the current number is exactly equal to a previous number.
        # 2. Add pairs where the current number is a permutation of a previous number.
        # To avoid double counting (if num is already a permutation of itself),
        # we use the principle of inclusion-exclusion or careful counting.
        
        # In 'Almost Equal Pairs II', the condition is usually:
        # (nums[i] == nums[j]) OR (nums[i] is a permutation of nums[j])
        
        # The number of existing elements that are permutations of 'num'
        # includes those that are exactly equal to 'num'.
        # Since the problem asks for 'almost equal' (which includes equal),
        # we simply count how many numbers seen so far share the same canonical form.
        
        total_pairs += permutation_counts[canonical]
        
        # Update the counts for future elements
        permutation_counts[canonical] += 1

    return total_pairs
