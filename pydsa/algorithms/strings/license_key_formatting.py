METADATA = {
    "id": 482,
    "name": "License Key Formatting",
    "slug": "license_key_formatting",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Format a license key string by grouping characters from right to left with dashes after every K characters.",
}

def solve(s: str, k: int) -> str:
    """Format a license key string by grouping characters from right to left with dashes after every K characters.

    Args:
        s (str): The input license key string containing alphanumeric characters and dashes.
        k (int): The number of characters per group (except possibly the first group).

    Returns:
        str: The formatted license key string with uppercase letters and dashes inserted every K characters from the right.

    Examples:
        >>> solve("5F3Z-2e-9-w", 4)
        '5F3Z-2E9W'
        >>> solve("2-5g-3-J", 2)
        '2-5G-3J'
    """
    # Remove all dashes and convert to uppercase
    cleaned = s.replace("-", "").upper()
    n = len(cleaned)
    
    # Calculate the length of the first group (which can be shorter than k)
    first_group_len = n % k
    if first_group_len == 0:
        first_group_len = k
    
    result = []
    
    # Add the first group (if it exists and is shorter than k)
    if first_group_len > 0 and first_group_len != n:
        result.append(cleaned[:first_group_len])
        result.append("-")
    
    # Process the rest of the string in chunks of size k
    for i in range(first_group_len, n, k):
        result.append(cleaned[i:i+k])
        result.append("-")
    
    # Remove the trailing dash if present
    if result and result[-1] == "-":
        result.pop()
    
    return "".join(result)