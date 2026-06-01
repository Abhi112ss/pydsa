METADATA = {
    "id": 831,
    "name": "Masking Personal Information",
    "slug": "masking_personal_information",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Mask sensitive information in emails or phone numbers based on specific formatting rules.",
}

def solve(information: str) -> str:
    """
    Masks personal information (email or phone number) based on its format.

    Rules:
    - If it's an email (contains '@'):
        - Keep the first character.
        - Keep the domain name (part after '@').
        - Mask all characters between the first character and the '@' with '*'.
    - If it's a phone number (contains only digits and possibly '-'):
        - Keep the first 3 digits.
        - Mask all subsequent digits with '*'.
        - Preserve the '-' characters in their original positions.

    Args:
        information: The input string representing either an email or a phone number.

    Returns:
        The masked version of the input string.

    Examples:
        >>> solve("a@example.com")
        'a@example.com'
        >>> solve("abc@def.com")
        'a**@def.com'
        >>> solve("123-456-7890")
        '123-***-****'
        >>> solve("1234567890")
        '123*******'
    """
    if "@" in information:
        # Handle Email Masking
        parts = information.split("@")
        local_part = parts[0]
        domain_part = parts[1]
        
        if len(local_part) <= 1:
            return information
        
        # Mask everything in local_part except the first character
        masked_local = local_part[0] + ("*" * (len(local_part) - 1))
        return f"{masked_local}@{domain_part}"
    
    else:
        # Handle Phone Number Masking
        result_chars = list(information)
        digit_count_seen = 0
        
        # We need to identify which characters are digits to mask them
        # but we must preserve the '-' characters.
        # The rule is: keep the first 3 digits, mask the rest.
        
        # First, count how many digits we have encountered to know when to start masking
        for i in range(len(result_chars)):
            if result_chars[i].isdigit():
                digit_count_seen += 1
                # If this is a digit and it's not among the first 3 digits, mask it
                if digit_count_seen > 3:
                    result_chars[i] = "*"
                    
        return "".join(result_chars)
