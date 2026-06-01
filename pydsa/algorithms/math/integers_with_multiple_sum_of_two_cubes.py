METADATA = {
    "id": 3890,
    "name": "Integers With Multiple Sum of Two Cubes",
    "slug": "integers_with_multiple_sum_of_two_cubes",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "number_theory"],
    "difficulty": "medium",
    "time_complexity": "O(n^(2/3))",
    "space_complexity": "O(n^(2/3))",
    "description": "Count how many integers up to n can be represented as a sum of two positive cubes in more than one way.",
}

def solve(n: int) -> int:
    """
    Counts the number of integers up to n that can be expressed as the sum 
    of two positive cubes (a^3 + b^3) in at least two distinct ways.

    Args:
        n (int): The upper bound (inclusive) for the integers to check.

    Returns:
        int: The count of integers <= n that have multiple representations.

    Examples:
        >>> solve(2000)
        1
        # 1729 = 1^3 + 12^3 = 9^3 + 10^3
    """
    if n < 1729:
        return 0

    # Dictionary to store the frequency of each sum of two cubes
    # Key: the sum (a^3 + b^3), Value: number of ways to form it
    sum_counts: dict[int, int] = {}

    # The maximum possible value for a or b is the cube root of n
    limit = int(n**(1/3)) + 2

    # Iterate through all pairs (a, b) such that a^3 + b^3 <= n
    # We use a <= b to avoid counting (a, b) and (b, a) as distinct pairs
    for a in range(1, limit):
        a_cubed = a**3
        if a_cubed >= n:
            break
            
        for b in range(a, limit):
            current_sum = a_cubed + b**3
            
            if current_sum > n:
                break
            
            # Increment the count for this specific sum
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1

    # Count how many sums appeared more than once
    multiple_sum_count = 0
    for count in sum_counts.values():
        if count > 1:
            multiple_sum_count += 1

    return multiple_sum_count
