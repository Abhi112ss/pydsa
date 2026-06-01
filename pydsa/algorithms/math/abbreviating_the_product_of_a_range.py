METADATA = {
    "id": 2117,
    "name": "Abbreviating the Product of a Range",
    "slug": "abbreviating_the_product_of_a_range",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the product of a range of integers, abbreviated with '...' if it exceeds a specific threshold.",
}

def solve(start: int, end: int, threshold: int) -> str:
    """
    Calculates the product of integers from start to end inclusive.
    If the product exceeds the threshold, returns the string '...'.

    Args:
        start: The starting integer of the range.
        end: The ending integer of the range.
        threshold: The maximum value allowed before abbreviation.

    Returns:
        A string representing the product or '...' if the product > threshold.

    Examples:
        >>> solve(1, 4, 100)
        '24'
        >>> solve(1, 10, 100)
        '...'
        >>> solve(0, 5, 10)
        '0'
    """
    # Handle the case where the range includes zero, as the product will always be zero
    # and zero is never greater than a non-negative threshold.
    if start <= 0 <= end:
        return "0"

    current_product = 1
    
    # Iterate through the range to calculate the product
    for i in range(start, end + 1):
        current_product *= i
        
        # Check if the running product has already exceeded the threshold
        # to avoid unnecessary large integer arithmetic and potential overflow
        if current_product > threshold:
            return "..."
            
    return str(current_product)
