METADATA = {
    "id": 899,
    "name": "Orderly Queue",
    "slug": "orderly-queue",
    "category": "String",
    "aliases": [],
    "tags": ["sorting", "greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine the lexicographically smallest string possible after performing a specific queue operation.",
}

def solve(s: str, k: int) -> str:
    """
    Finds the lexicographically smallest string possible by performing the 
    orderly queue operation.

    The operation involves picking an element, moving it to the front, 
    and shifting the remaining elements.

    Args:
        s: The input string.
        k: The number of elements that can be moved to the front.

    Returns:
        The lexicographically smallest string achievable.

    Examples:
        >>> solve("cba", 2)
        'abc'
        >>> solve("cba", 1)
        'bac'
    """
    # Case 1: If k == 1, the only possible operations are cyclic rotations.
    # We must check all possible rotations and pick the smallest one.
    if k == 1:
        n = len(s)
        smallest_rotation = s
        # Generate all n possible rotations
        for i in range(1, n):
            current_rotation = s[i:] + s[:i]
            if current_rotation < smallest_rotation:
                smallest_rotation = current_rotation
        return smallest_rotation

    # Case 2: If k > 1, we can perform a bubble sort-like mechanism.
    # By picking elements and moving them to the front, we can effectively
    # achieve any permutation of the string. Therefore, the smallest 
    # permutation is simply the sorted version of the string.
    return "".join(sorted(list(s)))
