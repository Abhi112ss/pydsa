METADATA = {
    "id": 2193,
    "name": "Minimum Number of Moves to Make Palindrome",
    "slug": "minimum-number-of-moves-to-make-palindrome",
    "category": "Greedy",
    "aliases": [],
    "tags": ["two_pointer", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of adjacent swaps required to transform a string into a palindrome.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of adjacent swaps to make a string a palindrome.

    The algorithm uses a greedy approach with two pointers. For each character 
    at the current left pointer, we find its matching counterpart from the 
    right side and swap it to the corresponding right position.

    Args:
        s: The input string.

    Returns:
        The minimum number of adjacent swaps required.

    Examples:
        >>> solve("aabb")
        2
        >>> solve("adamm")
        4
    """
    # Convert string to list because strings are immutable in Python
    chars = list(s)
    left = 0
    right = len(chars) - 1
    total_swaps = 0

    while left < right:
        # Find the rightmost character that matches chars[left]
        match_idx = right
        while match_idx > left and chars[match_idx] != chars[left]:
            match_idx -= 1

        if match_idx == left:
            # This character is the unique middle element in an odd-length palindrome.
            # Instead of moving it now, we swap it with its neighbor and 
            # try to find a match for the current left position again.
            # This effectively defers the middle element to the center.
            chars[left], chars[left + 1] = chars[left + 1], chars[left]
            total_swaps += 1
            # Do not increment 'left' yet; we need to find a match for the new chars[left]
            continue
        else:
            # Move the matching character from match_idx to the 'right' position
            # using adjacent swaps.
            while match_idx < right:
                chars[match_idx], chars[match_idx + 1] = chars[match_idx + 1], chars[match_idx]
                total_swaps += 1
                match_idx += 1
            
            # Move pointers inward after a successful match and swap
            left += 1
            right -= 1

    return total_swaps
