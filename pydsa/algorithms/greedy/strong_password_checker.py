METADATA = {
    "id": 420,
    "name": "Strong Password Checker",
    "slug": "strong-password-checker",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine the minimum number of operations to make a password strong based on length, character variety, and repeating sequences.",
}

def solve(password: str, min_length: int, max_length: int, has_lower: bool, has_upper: bool, has_digit: bool) -> int:
    """
    Args:
        password: The input password string.
        min_length: Minimum required length.
        max_length: Maximum allowed length.
        has_lower: Boolean indicating if lowercase is required.
        has_upper: Boolean indicating if uppercase is required.
        has_digit: Boolean indicating if digits are required.

    Returns:
        The minimum number of operations required.
    """
    n = len(password)
    
    if n < min_length:
        groups = []
        i = 0
        while i < n:
            count = 1
            while i + 1 < n and password[i] == password[i + 1]:
                count += 1
                i += 1
            groups.append(count)
            i += 1
        
        deletions_needed = 0
        replacements_needed = 0
        
        for count in groups:
            deletions_needed += count % 3
            replacements_needed += count // 3
            
        if replacements_needed >= (min_length - n):
            return min_length - n
        else:
            return max(min_length - n, deletions_needed + replacements_needed)

    if n > max_length:
        return n - max_length

    replacements_needed = 0
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and password[i] == password[i + 1]:
            count += 1
            i += 1
        replacements_needed += count // 3
        i += 1

    missing_types = 0
    if not has_lower:
        missing_types += 1
    if not has_upper:
        missing_types += 1
    if not has_digit:
        missing_types += 1

    return max(missing_types, replacements_needed)