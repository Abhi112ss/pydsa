METADATA = {
    "id": 1641,
    "name": "Count Sorted Vowel Strings",
    "slug": "count-sorted-vowel-strings",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Count the number of strings of length n that consist only of vowels and are sorted in non-decreasing order.",
}

import math

def solve(n: int) -> int:
    """
    Calculates the number of sorted vowel strings of length n using combinatorics.

    The problem asks for the number of ways to choose n vowels from the set {a, e, i, o, u}
    such that the order is non-decreasing. This is equivalent to the "Stars and Bars" 
    problem (combinations with replacement).
    
    We have k = 5 categories (vowels) and we need to choose n items.
    The formula for combinations with replacement is:
    C(n + k - 1, k - 1) or C(n + k - 1, n)

    Args:
        n: The length of the vowel string.

    Returns:
        The total number of sorted vowel strings of length n.

    Examples:
        >>> solve(1)
        5
        >>> solve(2)
        15
        >>> solve(3)
        35
    """
    # Number of available vowels
    vowel_count = 5
    
    # Using the Stars and Bars formula:
    # We need to choose n items from k categories where order doesn't matter 
    # (because we sort them) and repetition is allowed.
    # Formula: (n + k - 1) choose (k - 1)
    
    # k - 1 is the number of 'bars' needed to separate the 5 categories
    k_minus_one = vowel_count - 1
    
    # Total items to arrange (n stars + k-1 bars)
    total_items = n + k_minus_one
    
    # Calculate combinations: C(total_items, k_minus_one)
    # math.comb is available in Python 3.8+ and is highly optimized
    return math.comb(total_items, k_minus_one)
