METADATA = {
    "id": 3081,
    "name": "Replace Question Marks in String to Minimize Its Value",
    "slug": "replace-question-marks-in-string-to-minimize-its-value",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "strings", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Replace question marks in a string with digits to minimize the difference between the maximum and minimum digits in the resulting string.",
}

def solve(s: str) -> int:
    """
    Replaces question marks in a string with digits to minimize the range 
    (max_digit - min_digit) of the final string.

    Args:
        s: A string containing digits '0'-'9' and question marks '?'.

    Returns:
        The minimum possible difference between the maximum and minimum 
        digits in the string after replacing all '?'.

    Examples:
        >>> solve("1?3")
        2
        >>> solve("??")
        0
        >>> solve("9?1")
        8
    """
    n = len(s)
    
    # Identify the existing range of digits in the string
    existing_min = 10
    existing_max = -1
    question_mark_count = 0
    
    for char in s:
        if char == '?':
            question_mark_count += 1
        else:
            digit = int(char)
            if digit < existing_min:
                existing_min = digit
            if digit > existing_max:
                existing_max = digit
                
    # Case 1: No question marks, the range is fixed
    if question_mark_count == 0:
        return existing_max - existing_min if existing_max != -1 else 0

    # Case 2: Only question marks, we can make all digits the same (e.g., all '0's)
    if existing_max == -1:
        return 0

    # Case 3: Greedy approach. 
    # We want to fill '?' such that the new min/max doesn't expand the current range too much.
    # The optimal strategy is to try to fill '?' with digits that are already within 
    # the [existing_min, existing_max] range, or if we must expand, expand by the smallest amount.
    
    # The possible minimum value in the final string can only be between 0 and existing_min.
    # The possible maximum value in the final string can only be between existing_max and 9.
    # However, since we want to minimize (max - min), we can iterate through all possible 
    # target minimums (low) and target maximums (high).
    
    # Actually, a more efficient way: The final range [L, R] must satisfy:
    # 1. L <= existing_min
    # 2. R >= existing_max
    # 3. All '?' must be filled with digits in [L, R]
    
    # Since we want to minimize R - L, and we know L <= existing_min and R >= existing_max,
    # the best L is either existing_min or something smaller, and best R is existing_max or something larger.
    # But wait, if we pick an L < existing_min, we are just increasing the range.
    # The only reason to pick L < existing_min is if we have '?' that we want to fill with 
    # something smaller than existing_min to potentially satisfy a constraint? 
    # No, the constraint is simply to minimize the range.
    
    # Let's refine: The final range [L, R] must contain all existing digits.
    # So L <= existing_min and R >= existing_max.
    # To minimize R - L, we should try to keep L as large as possible and R as small as possible.
    # The largest possible L is existing_min. The smallest possible R is existing_max.
    # If we can fill all '?' with digits in [existing_min, existing_max], the answer is existing_max - existing_min.
    # If we can't (which is always true, we can always pick a digit in that range), 
    # the only way to get a smaller range is if we didn't have existing digits.
    
    # Wait, the problem is simpler: we can pick ANY digit for '?'.
    # To minimize max - min:
    # If we pick a digit 'd' for all '?', the new min is min(existing_min, d) 
    # and the new max is max(existing_max, d).
    # We want to minimize max(existing_max, d) - min(existing_min, d).
    
    # Let's test all possible digits d from 0 to 9 for the '?' marks.
    # Note: This assumes all '?' are filled with the SAME digit. 
    # Is it possible that filling '?' with different digits is better?
    # No, because if we use different digits, we only increase the range.
    # So all '?' should be filled with the same digit 'd'.
    
    min_range = 10
    for d in range(10):
        current_min = min(existing_min, d)
        current_max = max(existing_max, d)
        min_range = min(min_range, current_max - current_min)
        
    return min_range
