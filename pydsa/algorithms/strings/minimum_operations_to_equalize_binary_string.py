METADATA = {
    "id": 3666,
    "name": "Minimum Operations to Equalize Binary String",
    "slug": "minimum-operations-to-equalize-binary-string",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all characters in a binary string identical.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of operations to make all characters in a 
    binary string equal to either '0' or '1'.

    An operation consists of flipping a character. To minimize operations, 
    we compare the cost of changing all characters to '0' versus changing 
    all characters to '1'.

    Args:
        s: A string consisting of '0's and '1's.

    Returns:
        The minimum number of flips required to make the string uniform.

    Examples:
        >>> solve("0101")
        2
        >>> solve("111")
        0
        >>> solve("0001")
        1
    """
    # Count the number of '1's in the string.
    # The number of '0's can be derived from the total length.
    count_ones = 0
    total_length = len(s)

    for char in s:
        if char == '1':
            count_ones += 1

    # Cost to make all characters '0' is the number of '1's present.
    cost_to_zero = count_ones
    
    # Cost to make all characters '1' is the number of '0's present.
    cost_to_one = total_length - count_ones

    # The minimum of these two costs is the optimal solution.
    return min(cost_to_zero, cost_to_one)
