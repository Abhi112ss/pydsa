METADATA = {
    "id": 3474,
    "name": "Lexicographically Smallest Generated String",
    "slug": "lexicographically-smallest-generated-string",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct the lexicographically smallest string of length n that satisfies the given character frequency and adjacency constraints.",
}

def solve(n: int, counts: dict[str, int]) -> str:
    """
    Constructs the lexicographically smallest string of length n using the 
    provided character counts, ensuring no two identical characters are adjacent.

    Args:
        n: The total length of the string to be generated.
        counts: A dictionary where keys are characters and values are their 
                required frequencies.

    Returns:
        The lexicographically smallest valid string. Returns an empty string 
        if no such string can be constructed.

    Examples:
        >>> solve(5, {'a': 3, 'b': 2})
        'ababa'
        >>> solve(3, {'a': 3})
        ''
    """
    # Total characters must sum up to n
    if sum(counts.values()) != n:
        return ""

    # To ensure we can always pick a character without violating the 
    # adjacency rule, we must check if any character's count exceeds 
    # the maximum possible capacity: (n + 1) // 2.
    max_freq = 0
    for char in counts:
        if counts[char] > (n + 1) // 2:
            return ""
        max_freq = max(max_freq, counts[char])

    result = []
    last_char = ""

    for i in range(n):
        # Sort characters alphabetically to ensure lexicographical smallest order
        sorted_chars = sorted(counts.keys())
        found = False

        for char in sorted_chars:
            # Rule 1: Cannot use the same character as the previous one
            # Rule 2: Must have remaining count for this character
            if char != last_char and counts[char] > 0:
                
                # Greedy Check: If we pick this character, will the remaining 
                # characters be able to form a valid string?
                # The most frequent remaining character must not exceed 
                # the remaining slots available (considering adjacency).
                
                # Temporarily decrement to simulate picking
                counts[char] -= 1
                remaining_len = n - 1 - i
                
                can_proceed = True
                if remaining_len > 0:
                    # Find the new max frequency among remaining characters
                    current_max_freq = 0
                    for c in counts:
                        if counts[c] > current_max_freq:
                            current_max_freq = counts[c]
                    
                    # If the most frequent character exceeds the limit for 
                    # the remaining length, this choice is invalid.
                    # The limit for remaining_len is (remaining_len + 1) // 2
                    # BUT, if the most frequent character is the same as the 
                    # one we just picked, it's even more restricted.
                    # However, the standard (rem + 1) // 2 covers the general case.
                    if current_max_freq > (remaining_len + 1) // 2:
                        can_proceed = False
                    
                    # Special case: if the most frequent character is the same 
                    # as the one we just placed, it cannot be placed in the 
                    # very next slot, effectively reducing its capacity.
                    # But since we already checked char != last_char, we just 
                    # need to ensure the remaining counts are valid.
                    if current_max_freq == (remaining_len + 1) // 2:
                        # If max_freq is at its limit, the next char MUST 
                        # be that max_freq char (unless it's the same as last_char)
                        # This is implicitly handled by the loop and the check.
                        pass

                if can_proceed:
                    result.append(char)
                    last_char = char
                    found = True
                    break
                else:
                    # Backtrack: restore count if this choice was invalid
                    counts[char] += 1

        if not found:
            return ""

    return "".join(result)
