METADATA = {
    "id": 3415,
    "name": "Find Products with Three Consecutive Digits",
    "slug": "find-products-with-three-consecutive-digits",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the products of all sequences of three consecutive digits in an array.",
}

def solve(digits: list[int]) -> list[int]:
    """
    Calculates the products of all sequences of three consecutive digits in the input list.

    Args:
        digits: A list of integers representing digits.

    Returns:
        A list of integers where each element is the product of three consecutive digits.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        [6, 24, 60]
        >>> solve([1, 1, 1])
        [1]
        >>> solve([1, 2])
        []
    """
    n = len(digits)
    # If there are fewer than 3 digits, no consecutive triplet exists.
    if n < 3:
        return []

    results = []
    
    # Iterate through the array up to the point where a triplet can still be formed.
    # The loop runs from index 0 to n-3 inclusive.
    for i in range(n - 2):
        # Calculate the product of the current digit and the next two digits.
        product = digits[i] * digits[i + 1] * digits[i + 2]
        results.append(product)
        
    return results
