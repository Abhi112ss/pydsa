METADATA = {
    "id": 2844,
    "name": "Minimum Operations to Make a Special Number",
    "slug": "minimum-operations-to-make-a-special-number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum operations to make a number special by ensuring no two adjacent digits are the same, where an operation is changing a digit to any other digit.",
}

def solve(n: int, k: int) -> int:
    """
    Calculates the minimum operations to make a number 'special'.
    A number is special if no two adjacent digits are the same.
    An operation consists of changing a digit to any other digit (0-9).

    Args:
        n: The input integer.
        k: The target digit to avoid (though the problem implies we just need 
           to ensure no two adjacent digits are the same, the standard 
           interpretation of this specific LeetCode problem type is 
           ensuring no two adjacent digits are equal).

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve(111, 2)
        1
        >>> solve(123, 4)
        0
    """
    # Convert number to string to iterate through digits easily
    digits = str(n)
    operations = 0
    length = len(digits)
    
    # We use a list of characters to allow modification if needed, 
    # though we can also just track the 'last_changed_digit'
    digit_list = list(digits)
    
    for i in range(1, length):
        # If the current digit is the same as the previous one
        if digit_list[i] == digit_list[i - 1]:
            operations += 1
            # To minimize future operations, we change the current digit 
            # to something that is neither the previous digit nor the next digit.
            # In a greedy approach, changing it to a 'dummy' value that 
            # won't match anything is sufficient.
            digit_list[i] = '#' 
            
    return operations
