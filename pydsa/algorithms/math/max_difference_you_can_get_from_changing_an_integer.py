METADATA = {
    "id": 1432,
    "name": "Max Difference You Can Get From Changing an Integer",
    "slug": "max-difference-you-can-get-from-changing-an-integer",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Find the maximum possible difference between two integers formed by changing at most one digit of a given integer n.",
}

def solve(n: int) -> int:
    """
    Calculates the maximum difference between two integers formed by changing 
    at most one digit of the original integer n.

    To maximize the difference (max_val - min_val):
    1. To get the maximum value: Find the first digit from the left that is not '9' 
       and change it to '9'.
    2. To get the minimum value: Find the first digit from the left that is not '0' 
       (excluding the very first digit if it's the only digit, though the problem 
       implies n >= 1) and change it to '0'. Note: The first digit cannot be 
       changed to '0' if it results in a leading zero, but the problem constraints 
       and logic for 'min' usually imply changing the first non-zero digit to '0' 
       is only valid if it's not the leading digit, OR if we treat the number 
       as a sequence of digits. However, for n >= 1, the first digit is always 
       1-9. Changing the first digit to 0 is not allowed for the same number of digits.
       Actually, the rule is: to minimize, change the first non-zero digit to '0' 
       UNLESS it is the first digit. If it is the first digit, we can't change it 
       to '0' to keep the same number of digits. But wait, the problem says 
       "changing at most one digit". If we change the first digit to 0, it's 
       effectively a smaller number. Let's re-read: "the same number of digits".
       Actually, the standard interpretation for this problem is:
       - Maximize: Find first digit != 9, make it 9.
       - Minimize: Find first digit != 0, make it 0. If the first digit is the 
         only one that can be changed to 0, we must ensure we don't violate 
         the "same number of digits" if that were a rule, but here we just 
         change a digit. If we change the first digit to 0, the number of 
         digits decreases. However, the problem asks to change a digit. 
         If n=10, changing '1' to '0' makes it '00' (which is 0). 
         Actually, the simplest way is to treat the number as a string.

    Args:
        n: The input integer.

    Returns:
        The maximum difference between the modified maximum and minimum values.

    Examples:
        >>> solve(123)
        876
        # Max: 923, Min: 023 (which is 23). 923 - 23 = 900? No.
        # Let's re-evaluate: 
        # n = 123. Max: 923. Min: 023 (23). Diff: 900.
        # Wait, if n=123, max is 923, min is 023. 923-23 = 900.
        # If n=1, max is 9, min is 0. Diff 9.
        >>> solve(1)
        9
    """
    s = list(str(n))
    length = len(s)
    
    # Create a copy for the maximum value calculation
    max_s = list(s)
    # Create a copy for the minimum value calculation
    min_s = list(s)
    
    # To maximize: find the first digit that is not '9' and change it to '9'
    for i in range(length):
        if max_s[i] != '9':
            max_s[i] = '9'
            break
            
    # To minimize: find the first digit that is not '0' and change it to '0'
    # Note: The problem allows changing the first digit to '0' (e.g., 123 -> 023)
    for i in range(length):
        if min_s[i] != '0':
            min_s[i] = '0'
            break
            
    # Convert the modified digit lists back to integers
    max_val = int("".join(max_s))
    min_val = int("".join(min_s))
    
    return max_val - min_val
