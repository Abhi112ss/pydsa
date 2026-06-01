METADATA = {
    "id": 3201,
    "name": "Find the Maximum Length of Valid Subsequence I",
    "slug": "find-the-maximum-length-of-valid-subsequence-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a subsequence where the sum of every two adjacent elements has the same parity.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum length of a subsequence where (sub[i] + sub[i+1]) % 2 
    is constant for all i.

    The condition (a + b) % 2 == k implies:
    1. If k = 0: All elements must have the same parity (all even or all odd).
    2. If k = 1: Elements must alternate parity (even, odd, even... or odd, even, odd...).

    Args:
        nums: A list of integers.

    Returns:
        The maximum length of a valid subsequence.

    Examples:
        >>> solve([0, 1, 2, 3, 4])
        5
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([1, 2, 1, 1, 2, 1, 2])
        5
    """
    # There are 4 possible patterns for (a + b) % 2:
    # 1. All elements are even (sum % 2 == 0)
    # 2. All elements are odd (sum % 2 == 0)
    # 3. Alternating: Even, Odd, Even, Odd... (sum % 2 == 1)
    # 4. Alternating: Odd, Even, Odd, Even... (sum % 2 == 1)

    # Count all evens and all odds for the "same parity" cases
    evens_count = 0
    odds_count = 0
    for num in nums:
        if num % 2 == 0:
            evens_count += 1
        else:
            odds_count += 1

    # Calculate the maximum length for alternating parity
    # We look for the longest subsequence that flips parity at every step
    alternating_count = 0
    last_parity = -1  # -1 indicates we haven't picked the first element yet

    # Pattern: Start with whatever comes first, then flip
    # We can actually simplify this: just track the length of the longest 
    # alternating sequence regardless of whether it starts with 0 or 1.
    
    # To find the longest alternating sequence:
    # We track two states: 
    # dp[0]: max length ending in an even number
    # dp[1]: max length ending in an odd number
    # But for alternating, we need to know the parity of the *previous* element.
    
    # Let's use a more direct approach for alternating:
    # length_ending_even[0] = length of alternating sequence ending in even, 
    # where the previous was odd.
    # length_ending_odd[1] = length of alternating sequence ending in odd, 
    # where the previous was even.
    
    # Actually, the simplest way to find the max alternating sequence:
    # We want to find the longest sequence where parity[i] != parity[i-1]
    alt_len = 0
    current_target_parity = -1 # We don't know if we start with 0 or 1
    
    # We can just track two specific alternating sequences:
    # 1. Starts with 0 (0, 1, 0, 1...)
    # 2. Starts with 1 (1, 0, 1, 0...)
    # Or even simpler: just greedily pick the next required parity.
    
    def get_max_alternating(start_parity: int) -> int:
        count = 0
        needed = start_parity
        for num in nums:
            if num % 2 == needed:
                count += 1
                needed = 1 - needed
        return count

    # The max alternating sequence could start with 0 or 1.
    # However, the greedy approach for "any" alternating sequence is:
    # If we see a parity different from the last one we picked, pick it.
    
    greedy_alt_len = 0
    last_parity = -1
    for num in nums:
        current_parity = num % 2
        if current_parity != last_parity:
            greedy_alt_len += 1
            last_parity = current_parity

    # The result is the maximum of:
    # - All evens
    # - All odds
    # - The longest alternating sequence
    return max(evens_count, odds_count, greedy_alt_len)
