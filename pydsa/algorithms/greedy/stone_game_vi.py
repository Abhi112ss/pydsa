METADATA = {
    "id": 1686,
    "name": "Stone Game VI",
    "slug": "stone-game-vi",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Alice and Bob take turns picking stones with two values; maximize the difference between Alice's and Bob's total values.",
}

def solve(alice_values: list[int], bob_values: list[int]) -> int:
    """
    Determines the maximum possible difference between Alice's and Bob's total values.

    The optimal strategy is to pick the stone that maximizes the immediate gain 
    for the current player while minimizing the potential gain for the opponent. 
    This is achieved by sorting stones based on the sum of their values (alice_i + bob_i).

    Args:
        alice_values: A list of integers representing the value Alice gets from each stone.
        bob_values: A list of integers representing the value Bob gets from each stone.

    Returns:
        The maximum difference (Alice's total - Bob's total).

    Examples:
        >>> solve([5, 4, 5], [4, 7, 6])
        1
        >>> solve([1, 1, 1], [1, 1, 1])
        0
    """
    n = len(alice_values)
    # Combine values into tuples and sort by the sum of values in descending order.
    # This greedy approach works because picking a stone with a high (a + b) 
    # maximizes the current player's gain and denies the opponent a large value.
    stones = []
    for i in range(n):
        stones.append((alice_values[i], bob_values[i]))
    
    # Sort stones by (alice_val + bob_val) descending
    stones.sort(key=lambda x: x[0] + x[1], reverse=True)

    alice_score = 0
    bob_score = 0

    # Simulate the game turn by turn
    for i in range(n):
        if i % 2 == 0:
            # Alice's turn
            alice_score += stones[i][0]
        else:
            # Bob's turn
            bob_score += stones[i][1]

    return alice_score - bob_score
