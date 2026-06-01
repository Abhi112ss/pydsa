METADATA = {
    "id": 984,
    "name": "String Without AAA or BBB",
    "slug": "string-without-aaa-or-bbb",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(a + b)",
    "space_complexity": "O(a + b)",
    "description": "Construct a string using 'a' and 'b' such that no three consecutive characters are the same, maximizing the total length.",
}

def solve(a: int, b: int) -> str:
    """
    Constructs the longest possible string using 'a' and 'b' such that 
    no three consecutive characters are identical.

    Args:
        a: The number of 'a' characters available.
        b: The number of 'b' characters available.

    Returns:
        A string representing the longest valid sequence.

    Examples:
        >>> solve(1, 1)
        'ab'
        >>> solve(10, 1)
        'aabaa'
        >>> solve(2, 2)
        'aabb'
    """
    result = []
    
    # We use a greedy approach: always try to pick the character 
    # that has more remaining count to prevent running out of 
    # the "buffer" character too early.
    while a > 0 or b > 0:
        # Check if we are forced to pick 'b' because the last two were 'a'
        if len(result) >= 2 and result[-1] == result[-2] == 'a':
            if b == 0:
                break
            result.append('b')
            b -= 1
        # Check if we are forced to pick 'a' because the last two were 'b'
        elif len(result) >= 2 and result[-1] == result[-2] == 'b':
            if a == 0:
                break
            result.append('a')
            a -= 1
        # Otherwise, pick the character with the higher remaining count
        elif a > b:
            result.append('a')
            a -= 1
        else:
            result.append('b')
            b -= 1
            
    return "".join(result)
