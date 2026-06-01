METADATA = {
    "id": 926,
    "name": "Flip String to Monotone Increasing",
    "slug": "flip-string-to-monotone-increasing",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "prefix_sum", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of flips required to make a binary string monotone increasing.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of flips to make the binary string monotone increasing.
    
    A string is monotone increasing if it contains no '1' followed by a '0'.
    The algorithm uses a greedy approach/dynamic programming to track the number 
    of flips needed as we iterate through the string.

    Args:
        s: A string consisting of '0's and '1's.

    Returns:
        The minimum number of flips required.

    Examples:
        >>> solve("00110")
        1
        >>> solve("010110")
        2
    """
    # flips_needed tracks the minimum flips required to keep the string 
    # monotone increasing up to the current index.
    flips_needed = 0
    # ones_count tracks how many '1's we have encountered so far.
    ones_count = 0

    for char in s:
        if char == '1':
            # If we see a '1', we don't need to flip it to maintain monotonicity
            # for the current prefix, but we increment our count of potential 
            # '1's that might need flipping later if a '0' appears.
            ones_count += 1
        else:
            # If we see a '0', we have two choices to maintain monotonicity:
            # 1. Flip this '0' to a '1' (cost: flips_needed + 1)
            # 2. Keep this '0' and flip all previous '1's to '0's (cost: ones_count)
            # We take the minimum of these two strategies.
            flips_needed = min(flips_needed + 1, ones_count)

    return flips_needed
