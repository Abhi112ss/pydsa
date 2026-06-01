METADATA = {
    "id": 3623,
    "name": "Count Number of Trapezoids I",
    "slug": "count-number-of-trapezoids-i",
    "category": "math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of ways to choose four points that form a trapezoid with two parallel sides.",
}

def solve(sides: list[int]) -> int:
    """
    Args:
        sides: A list of integers representing the lengths of segments.

    Returns:
        The total number of ways to form a trapezoid.
    """
    n = len(sides)
    MOD = 10**9 + 7
    
    side_counts = {}
    for length in sides:
        side_counts[length] = side_counts.get(length, 0) + 1
        
    unique_lengths = list(side_counts.keys())
    total_trapezoids = 0
    
    for i in range(len(unique_lengths)):
        len_a = unique_lengths[i]
        count_a = side_counts[len_a]
        
        if count_a >= 2:
            ways_a = (count_a * (count_a - 1)) // 2
            
            for j in range(i, len(unique_lengths)):
                len_b = unique_lengths[j]
                count_b = side_counts[len_b]
                
                if len_a == len_b:
                    if count_a >= 4:
                        ways_b = (count_a * (count_a - 1) * (count_a - 2) * (count_a - 3)) // 24
                        total_trapezoids = (total_trapezoids + ways_b) % MOD
                else:
                    if count_b >= 2:
                        ways_b = (count_b * (count_b - 1)) // 2
                        total_trapezoids = (total_trapezoids + ways_a * ways_b) % MOD
                        
    return total_trapezoids