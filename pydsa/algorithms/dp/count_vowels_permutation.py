METADATA = {
    "id": 1220,
    "name": "Count Vowels Permutation",
    "slug": "count-vowels-permutation",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of valid vowel sequences of length n based on specific transition rules.",
}

def solve(n: int) -> int:
    """
    Calculates the number of valid vowel permutations of length n.

    The rules for transitions are:
    - 'a' can follow 'e'
    - 'e' can follow 'a' or 'i'
    - 'i' can follow 'a' or 'u'
    - 'o' can follow 'i' or 'u'
    - 'u' can follow 'a' or 'e' or 'i' or 'o'

    Args:
        n: The length of the vowel sequence.

    Returns:
        The total number of valid permutations modulo 10^9 + 7.

    Examples:
        >>> solve(1)
        5
        >>> solve(2)
        10
        >>> solve(5)
        68
    """
    MOD = 1_000_000_007

    if n == 1:
        return 5

    # Initial counts for n=1: one of each vowel
    count_a = 1
    count_e = 1
    count_i = 1
    count_o = 1
    count_u = 1

    # Iterate from 2 to n to build up the counts using DP
    for _ in range(2, n + 1):
        # Calculate next state based on the rules:
        # next_a: can follow 'e'
        # next_e: can follow 'a' or 'i'
        # next_i: can follow 'a' or 'u'
        # next_o: can follow 'i' or 'u'
        # next_u: can follow 'a', 'e', 'i', or 'o'
        
        new_a = count_e % MOD
        new_e = (count_a + count_i) % MOD
        new_i = (count_a + count_u) % MOD
        new_o = (count_i + count_u) % MOD
        new_u = (count_a + count_e + count_i + count_o) % MOD

        # Update current counts for the next iteration
        count_a, count_e, count_i, count_o, count_u = (
            new_a, new_e, new_i, new_o, new_u
        )

    return (count_a + count_e + count_i + count_o + count_u) % MOD
