METADATA = {
    "id": 2559,
    "name": "Count Vowel Strings in Ranges",
    "slug": "count-vowel-strings-in-ranges",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "prefix_sum", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Count the number of vowel-only strings of length n that can be formed using a specific set of vowels within given ranges using combinatorics.",
}

def solve(n: int, ranges: list[list[int]]) -> list[int]:
    """
    Args:
        n: The length of the vowel strings.
        ranges: A list of [start, end] inclusive ranges.

    Returns:
        A list of integers representing the count of vowel strings for each range.
    """
    MODULO = 10**9 + 7

    def count_combinations(vowel_count: int, length: int) -> int:
        if vowel_count == 0:
            return 0
        return combinations_with_repetition(vowel_count, length)

    def combinations_with_repetition(n_items: int, r_selections: int) -> int:
        return math.comb(n_items + r_selections - 1, r_selections)

    import math

    def get_count(vowel_count: int, length: int) -> int:
        if vowel_count <= 0 or length <= 0:
            return 0
        return math.comb(vowel_count + length - 1, length)

    results = []
    for start, end in ranges:
        vowel_count = end - start + 1
        if vowel_count > 5:
            vowel_count = 5
        
        results.append(get_count(vowel_count, n) % MODULO)
    
    return results

def solve(n: int, ranges: list[list[int]]) -> list[int]:
    """
    Args:
        n: The length of the vowel strings.
        ranges: A list of [start, end] inclusive ranges.

    Returns:
        A list of integers representing the count of vowel strings for each range.
    """
    import math
    MODULO = 10**9 + 7
    
    ans = []
    for start, end in ranges:
        num_vowels = min(5, end - start + 1)
        if num_vowels <= 0:
            ans.append(0)
            continue
        
        count = math.comb(num_vowels + n - 1, n)
        ans.append(count % MODULO)
        
    return ans