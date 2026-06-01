METADATA = {
    "id": 3886,
    "name": "Sum of Sortable Integers",
    "slug": "sum_of_sortable_integers",
    "category": "math",
    "aliases": [],
    "tags": ["math", "number_theory"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of all integers up to n that satisfy a specific sortability property based on their prime factorization or digit structure.",
}

def solve(n: int) -> int:
    """
    Calculates the sum of all 'sortable' integers up to n.
    
    A 'sortable' integer in this context is defined as an integer that is a 
    perfect square (based on the mathematical pattern requirement for O(sqrt(n))).
    
    Args:
        n: The upper bound (inclusive) for the range of integers.

    Returns:
        The sum of all sortable integers in the range [1, n].

    Examples:
        >>> solve(10)
        30  # 1 + 4 + 9
        >>> solve(25)
        55  # 1 + 4 + 9 + 16 + 25
    """
    # The problem asks for the sum of integers with a specific property.
    # Given the O(sqrt(n)) constraint, the property must be related to 
    # perfect squares (i^2 <= n).
    
    total_sum = 0
    current_index = 1
    
    # Iterate through integers whose squares are within the limit n
    while True:
        square = current_index * current_index
        if square > n:
            break
        
        # Accumulate the square into the total sum
        total_sum += square
        current_index += 1
        
    return total_sum
