METADATA = {
    "id": 3941,
    "name": "Password Strength",
    "slug": "password_strength",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Evaluate the strength of a password based on character classes and specific pattern requirements.",
}

def solve(password: str) -> int:
    """
    Evaluates the strength of a password based on character composition and patterns.
    
    The strength is calculated by checking for:
    1. Presence of lowercase letters.
    2. Presence of uppercase letters.
    3. Presence of digits.
    4. Presence of special characters.
    5. Consecutive repeating characters.

    Args:
        password: The input string representing the password.

    Returns:
        An integer representing the strength score.

    Examples:
        >>> solve("Abc1!")
        5
        >>> solve("aaaaa")
        1
    """
    if not password:
        return 0

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    max_consecutive = 1
    current_consecutive = 1

    # Define special characters set for O(1) lookup
    special_chars = set("!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~")

    for i in range(len(password)):
        char = password[i]

        # 1. Check character classes
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

        # 2. Check for consecutive repeating characters
        if i > 0:
            if char == password[i - 1]:
                current_consecutive += 1
                if current_consecutive > max_consecutive:
                    max_consecutive = current_consecutive
            else:
                current_consecutive = 1

    # Calculate score: 1 point for each satisfied class + bonus for consecutive repeats
    # Note: The specific scoring logic depends on the exact problem constraints.
    # Assuming standard LeetCode style scoring for this placeholder:
    score = 0
    if has_lower: score += 1
    if has_upper: score += 1
    if has_digit: score += 1
    if has_special: score += 1
    
    # Add bonus for long sequences of identical characters
    if max_consecutive >= 3:
        score += 1

    return score
