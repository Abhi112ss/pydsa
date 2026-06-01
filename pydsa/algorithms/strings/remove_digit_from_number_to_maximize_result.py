METADATA = {
    "id": 2259,
    "name": "Remove Digit From Number to Maximize Result",
    "slug": "remove-digit-from-number-to-maximize-result",
    "category": "Greedy",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove exactly one digit from a number represented as a string to make the resulting number as large as possible.",
}

def solve(number: str) -> str:
    """
    Removes one digit from the given number string to maximize the resulting number.

    The optimal strategy is to find the first digit that is strictly smaller than 
    the digit immediately following it. Removing such a digit increases the 
    value of the digit at that position by shifting a larger digit into it.
    If no such digit exists (the number is in non-increasing order), remove 
    the last digit.

    Args:
        number: A string representing a large positive integer.

    Returns:
        A string representing the maximum possible number after removing one digit.

    Examples:
        >>> solve("123")
        '23'
        >>> solve("555")
        '55'
        >>> solve("100")
        '10'
        >>> solve("4321")
        '432'
    """
    n = len(number)
    index_to_remove = n - 1

    # Iterate through the string to find the first occurrence where 
    # the current digit is less than the next digit.
    for i in range(n - 1):
        if number[i] < number[i + 1]:
            index_to_remove = i
            break

    # Construct the new number by slicing out the identified index.
    # This is O(n) due to string concatenation/slicing.
    result_list = list(number)
    result_list.pop(index_to_remove)
    
    return "".join(result_list)
