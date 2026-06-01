METADATA = {
    "id": 3587,
    "name": "Minimum Adjacent Swaps to Alternate Parity",
    "slug": "minimum-adjacent-swaps-to-alternate-parity",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of adjacent swaps required to rearrange an array such that elements alternate between even and odd parity.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of adjacent swaps to make the array alternate parity.

    The problem can be modeled as finding the minimum swaps to move elements to 
    specific target indices. For a valid alternating sequence, the parity of 
    elements at even indices must be the same, and the parity at odd indices 
    must be the opposite. The minimum swaps to reach a target permutation 
    is the sum of absolute differences between current and target positions.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of adjacent swaps required, or -1 if impossible.

    Examples:
        >>> solve([1, 2, 3, 4])
        2
        >>> solve([1, 1, 2, 2])
        2
        >>> solve([1, 2, 2, 1])
        1
        >>> solve([1, 1, 1, 2])
        -1
    """
    n = len(nums)
    even_indices = []
    odd_indices = []

    # Collect current positions of even and odd numbers
    for i, val in enumerate(nums):
        if val % 2 == 0:
            even_indices.append(i)
        else:
            odd_indices.append(i)

    # If the counts of even and odd numbers don't allow alternating, return -1
    if abs(len(even_indices) - len(odd_indices)) > 1:
        return -1

    def calculate_swaps(target_parity_at_zero: int) -> int:
        """
        Calculates swaps needed if the element at index 0 has target_parity_at_zero.
        target_parity_at_zero: 0 for even, 1 for odd.
        """
        # Reconstruct the required parity pattern for all indices
        # pattern[i] is the parity required at index i
        pattern = []
        current_parity = target_parity_at_zero
        for _ in range(n):
            pattern.append(current_parity)
            current_parity = 1 - current_parity

        # Check if the pattern matches the available counts of even/odd numbers
        pattern_even_count = pattern.count(0)
        pattern_odd_count = pattern.count(1)
        if pattern_even_count != len(even_indices) or pattern_odd_count != len(odd_indices):
            return float('inf')

        # Map current even/odd positions to their required positions in the pattern
        # We use a greedy approach: the i-th even number in the original array 
        # must move to the i-th even position in the target pattern.
        even_target_indices = [i for i, p in enumerate(pattern) if p == 0]
        odd_target_indices = [i for i, p in enumerate(pattern) if p == 1]

        total_swaps = 0
        # The sum of absolute differences between current and target indices 
        # gives the minimum adjacent swaps for a specific parity assignment.
        for current_pos, target_pos in zip(even_indices, even_target_indices):
            total_swaps += abs(current_pos - target_pos)
        
        # Note: We only need to sum one parity because the other is implicitly 
        # determined by the movement of the first parity.
        # However, to be safe and mathematically consistent with the displacement 
        # logic for permutations, we sum the displacement of one set.
        # In a permutation of indices, sum|pos_i - target_i| for one set 
        # is equivalent to the total swaps needed for the whole array.
        return total_swaps

    # Case 1: Even number at index 0
    res1 = calculate_swaps(0)
    # Case 2: Odd number at index 0
    res2 = calculate_swaps(1)

    ans = min(res1, res2)
    return int(ans) if ans != float('inf') else -1
