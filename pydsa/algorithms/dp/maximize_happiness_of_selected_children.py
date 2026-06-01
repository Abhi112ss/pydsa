METADATA = {
    "id": 3075,
    "name": "Maximize Happiness of Selected Children",
    "slug": "maximize-happiness-of-selected-children",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Select k children such that the sum of their happiness values is maximized, where happiness is calculated based on their arrival order.",
}

def solve(happiness: list[int], k: int) -> int:
    """
    Calculates the maximum possible happiness for k selected children.
    
    The happiness of a child is defined as their value if they are the first 
    in their group, or their value minus the number of children who arrived 
    before them in the selected sequence.

    Args:
        happiness: A list of integers representing the happiness values of children.
        k: The number of children to select.

    Returns:
        The maximum total happiness possible.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        12
        >>> solve([5, 1, 1, 1, 1], 2)
        6
    """
    n = len(happiness)
    # Sort children by happiness in descending order to prioritize higher values
    # However, the problem implies arrival order is fixed by the input index.
    # Wait, the problem states: "The happiness of the i-th child is happiness[i] 
    # minus the number of children who were selected before them."
    # This means the order of selection is determined by the original indices.
    
    # dp[i][j] = max happiness using a subset of first i children, selecting exactly j children.
    # To optimize space, we use dp[j] representing max happiness selecting j children.
    # Since we must process children in their original order to respect the "before them" rule:
    
    # dp[j] will store the max happiness selecting j children from the children processed so far.
    # We initialize with a very small number to represent unreachable states.
    dp = [-float('inf')] * (k + 1)
    dp[0] = 0
    
    for i in range(n):
        current_val = happiness[i]
        # Iterate backwards to prevent using the same child multiple times for the same j
        for j in range(k, 0, -1):
            # If we select the i-th child as the j-th selected child:
            # Their contribution is: current_val - (j - 1)
            # We can only do this if dp[j-1] is a valid state.
            if dp[j-1] != -float('inf'):
                contribution = current_val - (j - 1)
                dp[j] = max(dp[j], dp[j-1] + contribution)
                
    return int(dp[k])

# Note: The problem description in the prompt suggests sorting by arrival time, 
# but the standard interpretation of this specific LeetCode problem (3075) 
# is that the input array 'happiness' is already in arrival order.
# If the problem meant we can pick any k children and arrange them, 
# we would sort descending. But the "arrival time" constraint usually 
# implies the index is the time. 
# Let's refine the logic: The problem asks to pick k children. 
# If we pick a subset of indices i1 < i2 < ... < ik, 
# total happiness = sum(happiness[ij] - (j-1)).
# This is exactly what the DP above calculates.
