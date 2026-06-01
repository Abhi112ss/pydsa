METADATA = {
    "id": 1945,
    "name": "Sum of Digits of String After Convert",
    "slug": "sum-of-digits-of-string-after-convert",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a string of digits into a sum of its digits repeatedly until the string length is 1.",
}

def solve(num: str) -> str:
    """
    Args:
        num: A string representing a large integer.

    Returns:
        A string representing the single digit resulting from the iterative summation process.
    """
    current_string = num
    
    while len(current_string) > 1:
        total_sum = 0
        for digit_char in current_string:
            total_sum += int(digit_char)
        current_string = str(total_sum)
        
    return current_string