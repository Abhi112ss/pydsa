METADATA = {
    "id": 3333,
    "name": "Find the Original Typed String II",
    "slug": "find_the_original_typed_string_ii",
    "category": "algorithms",
    "aliases": [],
    "tags": ["dp", "combinatorics", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of possible original strings that could produce the given typed string where each original character may be repeated consecutively.",
}

MOD = 1_000_000_007

def solve() -> None:
    """Counts the number of possible original strings for a typed string.

    The typed string is formed by taking an original string and, for each
    character, repeating it a positive number of times consecutively.
    Different ways of grouping consecutive identical characters correspond to
    different possible original strings.

    Args:
        None. The function reads from standard input:
        - A single line containing the typed string `s`.

    Returns:
        None. Prints the count modulo 1_000_000_007.

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("abbc\\n")
        >>> solve()
        4
        Explanation: The typed string "abbc" can be split as:
        ["a","b","b","c"], ["a","bb","c"], ["a","b","bc"], ["a","bb","c"] (duplicate removed),
        resulting in 4 distinct original strings.
    """
    import sys

    s = sys.stdin.readline().strip()
    n = len(s)

    # dp[i] = number of