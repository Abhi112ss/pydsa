METADATA = {
    "id": 267,
    "name": "Palindrome Permutation II",
    "slug": "palindrome_permutation_ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "strings", "permutations"],
    "difficulty": "hard",
    "time_complexity": "O(n * n!)",
    "space_complexity": "O(n)",
    "description": "Find all unique palindromic permutations of a given string.",
}

def solve(s: str) -> list[str]:
    """
    Finds all unique palindromic permutations of a given string.

    Args:
        s: The input string.

    Returns:
        A list of all unique palindromic permutations.

    Examples:
        >>> solve("aabb")
        ['abba', 'baab']
        >>> solve("abc")
        []
    """
    char_counts: dict[str, int] = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_chars = [char for char, count in char_counts.items() if count % 2 != 0]

    # A palindrome can have at most one character with an odd frequency
    if len(odd_chars) > 1:
        return []

    middle_char = odd_chars[0] if odd_chars else ""
    
    # Build the pool of characters for the first half of the palindrome
    half_chars_pool: list[str] = []
    for char, count in char_counts.items():
        # We only need half of the occurrences for the left side
        half_chars_pool.extend([char] * (count // 2))

    results: list[str] = []
    used: list[bool] = [False] * len(half_chars_pool)
    # Sort to handle duplicates easily during backtracking
    half_chars_pool.sort()

    def backtrack(current_half: list[str]) -> None:
        if len(current_half) == len(half_chars_pool):
            # Construct the full palindrome: left + middle + reversed_left
            left_side = "".join(current_half)
            right_side = left_side[::-1]
            results.append(left_side + middle_char + right_side)
            return

        for i in range(len(half_chars_pool)):
            # Skip if this index is already used in the current permutation
            if used[i]:
                continue
            
            # Skip duplicate characters at the same recursion level to ensure uniqueness
            if i > 0 and half_chars_pool[i] == half_chars_pool[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            current_half.append(half_chars_pool[i])
            
            backtrack(current_half)
            
            # Backtrack: undo the choice
            current_half.pop()
            used[i] = False

    backtrack([])
    return results
