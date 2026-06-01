METADATA = {
    "id": 3937,
    "name": "Minimum Operations to Make Array Modulo Alternating I",
    "slug": "minimum-operations-to-make-array-modulo-alternating-i",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make an array follow an alternating modulo pattern.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum number of operations to make the array follow 
    an alternating pattern where elements at even indices have one remainder 
    and elements at odd indices have another remainder modulo k.

    Note: Based on the problem context of 'alternating modulo', the goal is 
    to make nums[i] % k == r1 if i is even and nums[i] % k == r2 if i is odd, 
    where r1 != r2. However, the standard interpretation for this specific 
    LeetCode pattern is making nums[i] % k equal to a fixed alternating 
    sequence of remainders.

    Args:
        nums: A list of integers.
        k: The modulo value.

    Returns:
        The minimum number of elements to change to satisfy the alternating condition.

    Examples:
        >>> solve([1, 2, 3, 4], 3)
        1
    """
    n = len(nums)
    if n == 0:
        return 0

    # We need to find two remainders r1 and r2 (0 <= r1, r2 < k) 
    # such that r1 != r2, to minimize changes.
    # Pattern 1: even indices % k == r1, odd indices % k == r2
    # Pattern 2: even indices % k == r2, odd indices % k == r1
    
    # Count frequencies of remainders at even and odd positions
    even_remainder_counts: dict[int, int] = {}
    odd_remainder_counts: dict[int, int] = {}
    
    even_total = 0
    odd_total = 0
    
    for i in range(n):
        rem = nums[i] % k
        if i % 2 == 0:
            even_remainder_counts[rem] = even_remainder_counts.get(rem, 0) + 1
            even_total += 1
        else:
            odd_remainder_counts[rem] = odd_remainder_counts.get(rem, 0) + 1
            odd_total += 1

    # To minimize changes, we maximize the number of elements we KEEP.
    # We want to pick r1 from even_remainder_counts and r2 from odd_remainder_counts
    # such that r1 != r2 and (even_remainder_counts[r1] + odd_remainder_counts[r2]) is max.
    
    max_kept = 0
    
    # Get the top two most frequent remainders for even and odd positions
    # to handle the constraint r1 != r2 efficiently.
    def get_top_two(counts: dict[int, int]) -> list[tuple[int, int]]:
        # Returns list of (remainder, frequency) sorted by frequency descending
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:2]

    top_even = get_top_two(even_remainder_counts)
    top_odd = get_top_two(odd_remainder_counts)
    
    # If no elements exist in a category, treat as 0 frequency
    if not top_even:
        top_even = [(0, 0)] # Dummy
    if not top_odd:
        top_odd = [(0, 0)] # Dummy

    # Check combinations of the most frequent remainders
    # Since we only care about the top 2, this is O(1) relative to k
    for r_even, count_even in top_even:
        for r_odd, count_odd in top_odd:
            if r_even != r_odd:
                max_kept = max(max_kept, count_even + count_odd)
            else:
                # If they are the same, we must pick the next best option
                # This is handled by the nested loops checking all top 2
                pass
                
    # Edge case: if k=1, r1 and r2 cannot be different. 
    # But the problem implies k > 1 for alternating remainders to exist.
    # If k is large, the top 2 approach is sufficient.
    # If all remainders are the same, we must pick a different r2.
    
    # If the best r_even == r_odd, we check:
    # 1. Best even + second best odd
    # 2. Second best even + best odd
    # This is already covered by the nested loops over top_even and top_odd.
    
    # If we couldn't find any r1 != r2 (e.g., k=1), 
    # the problem constraints usually prevent this or define behavior.
    # For k > 1, there's always a way.
    
    # If max_kept is still 0 and n > 0, it means we couldn't satisfy r1 != r2.
    # This only happens if k=1.
    if k == 1:
        return n # Or as per specific problem rules for k=1
        
    return n - max_kept
