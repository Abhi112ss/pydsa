METADATA = {
    "id": 1411,
    "name": "Number of Ways to Paint N x 3 Grid",
    "slug": "number-of-ways-to-paint-n-x-3-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to paint an n x 3 grid such that no two adjacent cells have the same color, using 3 colors.",
}

def solve(n: int) -> int:
    """
    Args:
        n: The number of rows in the grid.

    Returns:
        The total number of ways to paint the grid modulo 10^9 + 7.
    """
    MOD = 1_000_000_007

    if n == 1:
        return 6

    pattern_aaa = 0
    pattern_aab = 0
    pattern_aba = 0
    pattern_abb = 0
    pattern_baa = 0
    pattern_bab = 0
    pattern_bba = 0
    pattern_bbb = 0

    pattern_aab = 3
    pattern_aba = 2
    pattern_abb = 2
    pattern_baa = 2
    pattern_bab = 2
    pattern_bba = 2

    for row in range(2, n + 1):
        new_aaa = (pattern_aba + pattern_baa) % MOD
        new_aab = (pattern_aba + pattern_abb + pattern_baa) % MOD
        new_aba = (pattern_aab + pattern_abb + pattern_bab) % MOD
        new_abb = (pattern_aab + pattern_aba + pattern_bab) % MOD
        new_baa = (pattern_baa + pattern_bab + pattern_bba) % MOD
        new_bab = (pattern_baa + pattern_bba + pattern_abb) % MOD
        new_bba = (pattern_bab + pattern_baa + pattern_abb) % MOD
        new_bbb = (pattern_bab + pattern_bba) % MOD

        pattern_aaa = new_aaa
        pattern_aab = new_aab
        pattern_aba = new_aba
        pattern_abb = new_abb
        pattern_baa = new_baa
        pattern_bab = new_bab
        pattern_bba = new_bba
        pattern_bbb = new_bbb

    total_ways = (pattern_aaa + pattern_aab + pattern_aba + pattern_abb + 
                  pattern_baa + pattern_bab + pattern_bba + pattern_bbb) % MOD
    
    return total_ways

def solve_optimized(n: int) -> int:
    """
    Args:
        n: The number of rows in the grid.

    Returns:
        The total number of ways to paint the grid modulo 10^9 + 7.
    """
    MOD = 1_000_000_007
    
    if n == 1:
        return 6
    
    type_two_same = 3
    type_three_diff = 2
    
    for _ in range(2, n + 1):
        new_type_two_same = (type_two_same * 1 + type_three_diff * 2) % MOD
        new_type_three_diff = (type_two_same * 2 + type_three_diff * 1) % MOD
        
        type_two_same = new_type_two_same
        type_three_diff = new_type_three_diff
        
    return (type_two_same * 3 + type_three_diff * 2) % MOD

def solve(n: int) -> int:
    """
    Args:
        n: The number of rows in the grid.

    Returns:
        The total number of ways to paint the grid modulo 10^9 + 7.
    """
    MOD = 1_000_000_007
    
    if n == 1:
        return 6
    
    two_same = 3
    three_diff = 2
    
    for _ in range(2, n + 1):
        next_two_same = (two_same * 1 + three_diff * 2) % MOD
        next_three_diff = (two_same * 2 + three_diff * 1) % MOD
        two_same, three_diff = next_two_same, next_three_diff
        
    return (two_same * 3 + three_diff * 2) % MOD