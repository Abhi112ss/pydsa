METADATA = {
    "id": 1635,
    "name": "Hopper Company Queries I",
    "slug": "hopper-company-queries-i",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(q)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to reach a target index given specific movement rules for a hopper.",
}

def solve(n: int, queries: list[list[int]]) -> list[int]:
    """
    Calculates the number of ways to reach a target index based on hopper rules.
    
    The hopper starts at index 0. In each step, it can move to index i+1 or i+2.
    The problem asks for the number of ways to reach index 'target' using exactly 'steps' moves.
    However, the problem description for 1635 is actually a variation of a combinatorics 
    problem where we need to find the number of ways to reach a target index using 
    exactly 'steps' moves, where each move is either +1 or +2.
    
    Wait, looking at the specific constraints of LeetCode 1635 (which is a variation 
    of the 'Hopper' problem):
    The rule is: a hopper can move from index i to i+1 or i+2.
    We need to find the number of ways to reach index 'target' in exactly 'steps' moves.
    
    Let x be the number of +2 moves and y be the number of +1 moves.
    1) x + y = steps (total moves)
    2) 2x + y = target (total distance)
    
    Subtracting (1) from (2):
    (2x + y) - (x + y) = target - steps
    x = target - steps
    
    Then:
    y = steps - x = steps - (target - steps) = 2 * steps - target
    
    For a valid solution:
    - x >= 0  => target >= steps
    - y >= 0  => 2 * steps >= target
    - x + y = steps (already used)
    
    The number of ways is the number of ways to arrange x moves of type +2 and y moves of type +1,
    which is the binomial coefficient C(steps, x) or C(steps, y).
    
    Args:
        n: The total number of indices (not strictly used in the math but part of input).
        queries: A list of queries where each query is [target, steps].
        
    Returns:
        A list of integers representing the number of ways for each query.
        
    Examples:
        >>> solve(5, [[3, 2], [3, 3]])
        [2, 1]
        # Query [3, 2]: target=3, steps=2. x = 3-2=1, y = 2-1=1. C(2, 1) = 2.
        # Query [3, 3]: target=3, steps=3. x = 3-3=0, y = 3-0=3. C(3, 0) = 1.
    """
    
    def combinations(n_val: int, k_val: int) -> int:
        """Calculates nCr using iterative approach."""
        if k_val < 0 or k_val > n_val:
            return 0
        if k_val == 0 or k_val == n_val:
            return 1
        if k_val > n_val // 2:
            k_val = n_val - k_val
            
        numerator = 1
        denominator = 1
        for i in range(k_val):
            numerator = numerator * (n_val - i)
            denominator = denominator * (i + 1)
        return numerator // denominator

    results = []
    for target, steps in queries:
        # Calculate number of +2 moves (x) and +1 moves (y)
        # x + y = steps
        # 2x + y = target
        x = target - steps
        y = steps - x
        
        # Check if the combination of moves is physically possible
        if x < 0 or y < 0:
            results.append(0)
        else:
            # The number of ways is the number of ways to choose 'x' positions 
            # for the +2 moves out of 'steps' total moves.
            results.append(combinations(steps, x))
            
    return results
