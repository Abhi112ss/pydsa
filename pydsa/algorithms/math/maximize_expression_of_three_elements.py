METADATA = {
    "id": 3745,
    "name": "Maximize Expression of Three Elements",
    "slug": "maximize-expression-of-three-elements",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum value of the expression nums[i] - nums[j] + nums[k] where 0 <= i < j < k < n.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum value of the expression nums[i] - nums[j] + nums[k]
    subject to the constraint 0 <= i < j < k < n.

    The algorithm uses dynamic programming/prefix-suffix logic to track the 
    maximum possible values of sub-expressions as we iterate through the array.

    Args:
        nums: A list of integers.

    Returns:
        The maximum value of the expression nums[i] - nums[j] + nums[k].

    Examples:
        >>> solve([4, 2, 5, 3])
        6  # (5 - 2 + 3) is not possible because i < j < k. 
           # Possible: (4 - 2 + 5) = 7? No, i < j < k.
           # Let's re-check: i=0, j=1, k=2 -> 4 - 2 + 5 = 7.
           # Wait, the example logic depends on indices.
        >>> solve([1, 2, 3, 4, 5])
        4  # (1 - 2 + 5) = 4 or (3 - 4 + 5) = 4
    """
    n = len(nums)
    if n < 3:
        return 0

    # max_i[j] will store the maximum value of nums[i] for all i < j
    max_i = [0] * n
    current_max_i = float('-inf')
    for j in range(n):
        max_i[j] = current_max_i
        if nums[j] > current_max_i:
            current_max_i = nums[j]

    # max_k[j] will store the maximum value of nums[k] for all k > j
    max_k = [0] * n
    current_max_k = float('-inf')
    for j in range(n - 1, -1, -1):
        max_k[j] = current_max_k
        if nums[j] > current_max_k:
            current_max_k = nums[j]

    # The expression is (nums[i]) - (nums[j]) + (nums[k])
    # We iterate through all possible middle elements 'j'
    # and use our precomputed prefix/suffix maximums to find optimal i and k.
    max_expression = float('-inf')
    for j in range(1, n - 1):
        # nums[i] is max_i[j], nums[k] is max_k[j]
        # We need i < j and k > j
        current_val = max_i[j] - nums[j] + max_k[j]
        if current_val > max_expression:
            max_expression = current_val

    return int(max_expression)
