METADATA = {
    "id": 1753,
    "name": "Maximum Score From Removing Stones",
    "slug": "maximum-score-from-removing-stones",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum number of stones that can be removed from two piles such that each removal involves one stone from each pile.",
}

def solve(stones: list[int]) -> int:
    """
    Calculates the maximum score obtainable by removing stones from two piles.
    
    The problem asks for the maximum number of pairs (one from each pile) we can 
    form. If one pile is significantly larger than the other, we are limited 
    by the smaller pile. If the piles are relatively balanced, we can 
    alternatingly pick stones until we have used almost all stones, 
    limited only by the total count divided by two.

    Args:
        stones: A list of two integers representing the number of stones in each pile.

    Returns:
        The maximum number of stones that can be removed.

    Examples:
        >>> solve([2, 4])
        2
        >>> solve([3, 3])
        3
        >>> solve([1, 10])
        1
    """
    pile_a = stones[0]
    pile_b = stones[1]
    
    # Identify the smaller and larger piles
    smaller_pile = min(pile_a, pile_b)
    larger_pile = max(pile_a, pile_b)
    
    # Case 1: The larger pile is so big that we can exhaust the smaller pile 
    # entirely by always picking one from the smaller and one from the larger.
    if larger_pile >= 2 * smaller_pile:
        return smaller_pile
    
    # Case 2: The piles are balanced enough that we can alternate between them.
    # In this case, we can take almost all stones. The maximum possible pairs 
    # is the floor of the total number of stones divided by 2.
    # Example: [3, 3] -> 6/2 = 3. [3, 4] -> 7/2 = 3.
    return (pile_a + pile_b) // 2
