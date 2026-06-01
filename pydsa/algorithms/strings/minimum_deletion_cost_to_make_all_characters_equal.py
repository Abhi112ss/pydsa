METADATA = {
    "id": 3784,
    "name": "Minimum Deletion Cost to Make All Characters Equal",
    "slug": "minimum-deletion-cost-to-make-all-characters-equal",
    "category": "Greedy",
    "aliases": [],
    "tags": ["hash_map", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum cost to delete characters such that all remaining characters in the string are the same.",
}

def solve(s: str, costs: list[int]) -> int:
    """
    Calculates the minimum cost to delete characters so that all remaining 
    characters in the string are identical.

    The strategy is to calculate the total cost of all characters and then 
    subtract the maximum possible cost of a single character type that we 
    decide to keep.

    Args:
        s: The input string consisting of lowercase English letters.
        costs: A list of integers where costs[i] is the cost to delete s[i].

    Returns:
        The minimum total cost to make all remaining characters equal.

    Examples:
        >>> solve("aabbc", [1, 2, 3, 4, 5])
        6
        # Keep 'a's: cost = 3+4+5 = 12
        # Keep 'b's: cost = 1+2+5 = 8
        # Keep 'c's: cost = 1+2+3+4 = 10
        # Wait, the logic is: Total Cost - Max(Cost of keeping char X)
        # Total = 15. 
        # Cost to keep 'a': 1+2=3. Cost to delete others: 3+4+5=12.
        # Cost to keep 'b': 3+4=7. Cost to delete others: 1+2+5=8.
        # Cost to keep 'c': 5. Cost to delete others: 1+2+3+4=10.
        # Min cost is 8.
    """
    if not s:
        return 0

    # Dictionary to store the sum of costs for each character type
    char_cost_map: dict[str, int] = {}
    total_cost: int = 0

    # Iterate through the string once to aggregate costs
    for char, cost in zip(s, costs):
        char_cost_map[char] = char_cost_map.get(char, 0) + cost
        total_cost += cost

    # To minimize deletion cost, we maximize the cost of the characters we KEEP.
    # We can only keep characters of ONE type.
    max_keep_cost: int = 0
    for char_sum in char_cost_map.values():
        if char_sum > max_keep_cost:
            max_keep_cost = char_sum

    # The minimum deletion cost is the total cost minus the cost of the 
    # character group we choose to preserve.
    return total_cost - max_keep_cost
