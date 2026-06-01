METADATA = {
    "id": 1291,
    "name": "Sequential Digits",
    "slug": "sequential-digits",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "enumeration", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find all positive integers with n digits that are made up of consecutive digits.",
}

def solve(n: int, low: int, high: int) -> list[int]:
    """
    Finds all n-digit sequential numbers within the range [low, high].

    Args:
        n: The number of digits required for each sequential number.
        low: The lower bound of the range (inclusive).
        high: The upper bound of the range (inclusive).

    Returns:
        A sorted list of integers that are n-digit sequential numbers within the range.

    Examples:
        >>> solve(2, 1, 22)
        [12]
        >>> solve(3, 100, 1000)
        [123, 234, 345, 456, 567, 678, 789]
    """
    # If n is greater than 9, no sequential digits can exist (digits are 1-9)
    if n > 9:
        return []

    results: list[int] = []
    digits_sequence = "123456789"

    # We iterate through the string '123456789' and take substrings of length n
    # The number of possible starting positions is (9 - n + 1)
    for i in range(10 - n):
        # Extract the substring of length n
        substring = digits_sequence[i : i + n]
        
        # Convert the substring to an integer
        sequential_num = int(substring)
        
        # Check if the generated number falls within the specified range
        if low <= sequential_num <= high:
            results.append(sequential_num)

    return results
