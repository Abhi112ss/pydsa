METADATA = {
    "id": 3848,
    "name": "Check Digitorial Permutation",
    "slug": "check-digitorial-permutation",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(1)",
    "description": "Determine if one number is a digitorial permutation of another by comparing digit frequencies.",
}

def solve(num1: int, num2: int) -> bool:
    """
    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.

    Returns:
        bool: True if num1 is a digitorial permutation of num2, False otherwise.
    """
    digit_counts = [0] * 10

    if num1 == 0:
        digit_counts[0] += 1
    else:
        temp_num1 = num1
        while temp_num1 > 0:
            digit_counts[temp_num1 % 10] += 1
            temp_num1 //= 10

    if num2 == 0:
        digit_counts[0] -= 1
    else:
        temp_num2 = num2
        while temp_num2 > 0:
            digit_counts[temp_num2 % 10] -= 1
            temp_num2 //= 10

    for count in digit_counts:
        if count != 0:
            return False

    return True