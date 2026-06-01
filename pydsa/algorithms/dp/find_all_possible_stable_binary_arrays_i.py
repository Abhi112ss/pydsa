METADATA = {
    "id": 3129,
    "name": "Find All Possible Stable Binary Arrays I",
    "slug": "find-all-possible-stable-binary-arrays-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of binary arrays of length n where no three consecutive elements are the same, modulo 10^9 + 7.",
}

def solve(n: int) -> int:
    """
    Calculates the number of stable binary arrays of length n.
    A stable binary array is defined as one where no three consecutive elements are identical.

    Args:
        n: The length of the binary array.

    Returns:
        The total number of stable binary arrays modulo 10^9 + 7.

    Examples:
        >>> solve(1)
        2
        >>> solve(2)
        4
        >>> solve(3)
        6
    """
    MOD = 1_000_000_007

    if n == 1:
        return 2
    if n == 2:
        return 4

    # Let dp0[i] be the number of stable arrays of length i ending in '0'
    # Let dp1[i] be the number of stable arrays of length i ending in '1'
    # However, to avoid three consecutive, we need to track if the last two are the same.
    # Let end_diff[i] be the number of stable arrays of length i where the last two elements are different.
    # Let end_same[i] be the number of stable arrays of length i where the last two elements are the same.
    
    # Base case for n = 2:
    # end_diff: [0, 1], [1, 0] -> 2
    # end_same: [0, 0], [1, 1] -> 2
    end_diff = 2
    end_same = 2

    # For n > 2, we iterate from 3 to n.
    # To form a stable array of length i:
    # 1. If we want the last two to be different (e.g., ...01 or ...10):
    #    The previous element must have been different from the current one.
    #    This can follow ANY stable array of length i-1.
    #    So, end_diff_new = end_diff_old + end_same_old
    # 2. If we want the last two to be the same (e.g., ...00 or ...11):
    #    The previous element must have been different from the one before it to avoid three in a row.
    #    So, end_same_new = end_diff_old
    
    for _ in range(3, n + 1):
        new_end_diff = (end_diff + end_same) % MOD
        new_end_same = end_diff % MOD
        
        end_diff = new_end_diff
        end_same = new_end_same

    return (end_diff + end_same) % MOD
