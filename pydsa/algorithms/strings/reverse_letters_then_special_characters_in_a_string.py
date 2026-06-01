METADATA = {
    "id": 3823,
    "name": "Reverse Letters Then Special Characters in a String",
    "slug": "reverse-letters-then-special-characters-in-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reverse the order of letters in a string while keeping special characters in their original positions.",
}

def solve(s: str) -> str:
    """
    Reverses the order of letters in a string while keeping non-letter 
    characters in their original positions.

    Args:
        s: The input string containing letters and special characters.

    Returns:
        A new string where letters are reversed but special characters 
        remain at their original indices.

    Examples:
        >>> solve("a-bC-d")
        'd-Cb-a'
        >>> solve("!ab@c")
        '!cb@a'
    """
    # Convert string to list because strings are immutable in Python
    char_list = list(s)
    left_index = 0
    right_index = len(char_list) - 1

    while left_index < right_index:
        # Move left pointer until a letter is found
        if not char_list[left_index].isalpha():
            left_index += 1
            continue
        
        # Move right pointer until a letter is found
        if not char_list[right_index].isalpha():
            right_index -= 1
            continue
        
        # Both pointers are at letters, so swap them
        char_list[left_index], char_list[right_index] = (
            char_list[right_index],
            char_list[left_index],
        )
        
        # Move both pointers inward after swap
        left_index += 1
        right_index -= 1

    return "".join(char_list)
