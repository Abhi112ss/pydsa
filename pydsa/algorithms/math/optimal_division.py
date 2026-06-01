METADATA = {
    "id": 553,
    "name": "Optimal Division",
    "slug": "optimal-division",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Maximize the result of a division sequence by grouping all terms after the first into a single denominator.",
}

def solve(expression: str) -> str:
    """
    Args:
        expression: A string representing a division sequence of numbers.

    Returns:
        A string representing the optimal division grouping.
    """
    numbers = []
    current_number = ""
    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            numbers.append(current_number)
            current_number = ""
    numbers.append(current_number)

    if len(numbers) <= 2:
        return expression

    first_number = numbers[0]
    remaining_numbers = numbers[1:]
    
    denominator_parts = []
    for i in range(len(remaining_numbers)):
        denominator_parts.append(remaining_numbers[i])
        if i < len(remaining_numbers) - 1:
            denominator_parts.append("/")
            
    denominator_string = "".join(denominator_parts)
    
    return f"{first_number}/({denominator_string})"