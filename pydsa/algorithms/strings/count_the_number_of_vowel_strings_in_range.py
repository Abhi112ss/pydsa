METADATA = {
    "id": 2586,
    "name": "Count the Number of Vowel Strings in Range",
    "slug": "count-the-number-of-vowel-strings-in-range",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Count the number of strings of length n consisting only of vowels that fall lexicographically within the range [low, high].",
}

def solve(n: int, low: str, high: str) -> int:
    """
    Counts the number of vowel strings of length n in the lexicographical range [low, high].

    The problem can be solved by calculating the number of vowel strings of length n 
    that are lexicographically less than or equal to a given string 's'.
    Since there are 5 vowels (a, e, i, o, u), we can treat this as a base-5 number system.

    Args:
        n: The length of the strings.
        low: The lower bound string (inclusive).
        high: The upper bound string (inclusive).

    Returns:
        The count of vowel strings in the range [low, high].

    Examples:
        >>> solve(3, "aaa", "aaa")
        1
        >>> solve(3, "aaa", "aae")
        2
        >>> solve(3, "aaa", "uuu")
        125
    """
    vowels = "aeiou"
    # Map each vowel to its rank (0-4)
    vowel_to_rank = {v: i for i, v in enumerate(vowels)}

    def count_upto(s: str) -> int:
        """
        Counts how many vowel strings of length n are lexicographically <= s.
        
        The logic follows a digit-by-digit approach similar to converting 
        a number from base-5 to decimal.
        """
        count = 0
        # We iterate through the string to determine how many combinations 
        # exist for the prefix.
        for i in range(n):
            rank = vowel_to_rank[s[i]]
            # For the current position i, we can pick any vowel with a rank 
            # strictly less than the rank of s[i]. 
            # For each such choice, all subsequent (n - 1 - i) positions 
            # can be any of the 5 vowels.
            count += rank * (5 ** (n - 1 - i))
        
        # The loop counts strings strictly less than s. 
        # We add 1 to include the string s itself.
        return count + 1

    # The number of strings in [low, high] is:
    # (strings <= high) - (strings < low)
    # Which is equivalent to: (strings <= high) - (strings <= low) + 1
    # Or more simply: count_upto(high) - count_upto(low) + 1
    # However, since count_upto(low) includes 'low', we subtract count_upto(low-1).
    # A cleaner way: count_upto(high) - count_upto_exclusive(low)
    
    def count_upto_exclusive(s: str) -> int:
        """Counts strings strictly less than s."""
        count = 0
        for i in range(n):
            rank = vowel_to_rank[s[i]]
            count += rank * (5 ** (n - 1 - i))
        return count

    return count_upto(high) - count_upto_exclusive(low)
