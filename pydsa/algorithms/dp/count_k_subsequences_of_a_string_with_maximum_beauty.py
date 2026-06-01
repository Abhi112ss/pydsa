METADATA = {
    "id": 2842,
    "name": "Count K-Subsequences of a String With Maximum Beauty",
    "slug": "count-k-subsequences-of-a-string-with-maximum-beauty",
    "category": "combinatorics",
    "aliases": [],
    "tags": ["math", "combinatorics", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subsequences that achieve the maximum possible beauty by selecting k characters of the same type.",
}

def solve(s: str, k: int) -> int:
    """
    Args:
        s: The input string.
        k: The number of characters to select for each subsequence.

    Returns:
        The number of subsequences with maximum beauty modulo 10^9 + 7.
    """
    MODULUS = 10**9 + 7
    frequency_map = {}
    for character in s:
        frequency_map[character] = frequency_map.get(character, 0) + 1

    max_frequency = 0
    for count in frequency_map.values():
        if count > max_frequency:
            max_frequency = count

    if max_frequency < k:
        return 0

    def combinations(n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        if r == 0 or r == n:
            return 1
        if r > n // 2:
            r = n - r
        
        numerator = 1
        denominator = 1
        for i in range(r):
            numerator = (numerator * (n - i)) % MODULUS
            denominator = (denominator * (i + 1)) % MODULUS
        
        return (numerator * pow(denominator, MODULUS - 2, MODULUS)) % MODULUS

    total_ways = 0
    for count in frequency_map.values():
        if count >= k:
            total_ways = (total_ways + combinations(count, k)) % MODULUS

    return total_ways