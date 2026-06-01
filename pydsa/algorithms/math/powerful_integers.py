METADATA = {
    "id": 970,
    "name": "Powerful Integers",
    "slug": "powerful-integers",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_set", "enumeration", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log_x(bound) * log_y(bound))",
    "space_complexity": "O(log_x(bound) * log_y(bound))",
    "description": "Find all integers up to a bound that can be expressed as the sum of a power of x and a power of y.",
}

def solve(x: int, y: int, bound: int) -> list[int]:
    """
    Finds all powerful integers up to a given bound.
    
    A powerful integer is an integer that can be expressed as the sum of 
    a power of x and a power of y (x^i + y^j where i, j >= 0).

    Args:
        x: The base of the first power.
        y: The base of the second power.
        bound: The upper limit (inclusive) for the sum.

    Returns:
        A sorted list of all unique powerful integers less than or equal to bound.

    Examples:
        >>> solve(2, 3, 10)
        [2, 3, 4, 5, 7, 9, 10]
        >>> solve(3, 7, 1)
        []
    """
    # Use a set to automatically handle duplicate sums (e.g., if x^i + y^j == x^a + y^b)
    powerful_set: set[int] = set()
    
    # Pre-calculate all powers of x that are <= bound
    x_powers: list[int] = []
    current_x_power = 1
    while current_x_power <= bound:
        x_powers.append(current_x_power)
        current_x_power *= x
        
    # Pre-calculate all powers of y that are <= bound
    y_powers: list[int] = []
    current_y_power = 1
    while current_y_power <= bound:
        y_powers.append(current_y_power)
        current_y_power *= y
        
    # Iterate through all combinations of x^i and y^j
    for px in x_powers:
        for py in y_powers:
            total_sum = px + py
            # Only add to set if the sum is within the allowed bound
            if total_sum <= bound:
                powerful_set.add(total_sum)
            else:
                # Since y_powers is sorted, if px + py > bound, 
                # larger py values will also exceed the bound.
                break
                
    return sorted(list(powerful_set))
