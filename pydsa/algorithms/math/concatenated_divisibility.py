METADATA = {
    "id": 3533,
    "name": "Concatenated Divisibility",
    "slug": "concatenated_divisibility",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string_manipulation", "modular_arithmetic"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Determine if there exists a subsequence of strings that, when concatenated, forms a number divisible by a given divisor.",
}

def solve(nums: list[int], divisor: int) -> bool:
    """
    Determines if any non-empty subsequence of numbers, when concatenated, 
    results in a number divisible by the given divisor.

    Args:
        nums: A list of integers to be concatenated.
        divisor: The integer divisor to check against.

    Returns:
        True if a subsequence exists whose concatenation is divisible by divisor, 
        False otherwise.

    Examples:
        >>> solve([12, 3], 3)
        True
        >>> solve([1, 2], 5)
        False
    """
    # We use dynamic programming to track reachable remainders.
    # reachable_remainders[r] is True if there is a subsequence 
    # whose concatenation results in a number congruent to r modulo divisor.
    reachable_remainders = [False] * divisor

    for num in nums:
        num_str = str(num)
        num_len = len(num_str)
        
        # Pre-calculate the remainder of the current number itself
        # and the multiplier needed to shift existing remainders.
        # If we append 'num' to a number 'X', the new number is X * 10^len(num) + num.
        current_num_rem = int(num_str) % divisor
        
        # Pre-calculate 10^len(num) % divisor
        shift_multiplier = pow(10, num_len, divisor)
        
        # To avoid using the same number multiple times in one subsequence 
        # (unless it's a different element in the list), we work on a copy.
        new_remainders = reachable_remainders[:]
        
        # Case 1: The current number starts a new subsequence
        new_remainders[current_num_rem] = True
        
        # Case 2: Append the current number to all previously reachable remainders
        for r in range(divisor):
            if reachable_remainders[r]:
                # New remainder = (old_remainder * 10^len(num) + current_num) % divisor
                new_rem = (r * shift_multiplier + current_num_rem) % divisor
                new_remainders[new_rem] = True
        
        reachable_remainders = new_remainders
        
        # Early exit if we found a subsequence divisible by divisor
        if reachable_remainders[0]:
            return True

    return reachable_remainders[0]
