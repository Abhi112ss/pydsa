METADATA = {
    "id": 3723,
    "name": "Maximize Sum of Squares of Digits",
    "slug": "maximize-sum-of-squares-of-digits",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible sum of the squares of digits of a number formed by rearranging or modifying digits to maximize the sum.",
}

def solve(n: int) -> int:
    """
    Calculates the maximum sum of squares of digits possible by transforming 
    the number into a form that maximizes digit values (typically involving nines).

    Args:
        n: The input integer.

    Returns:
        The maximum sum of squares of digits.

    Examples:
        >>> solve(10)
        1
        >>> solve(432)
        18  # (9^2 + 3^2 = 81 + 9 = 90 is not possible, but 4^2+3^2+2^2=29. 
            # Wait, the logic for this specific problem type usually involves 
            # comparing the original sum vs a number like 99...9 and a leading digit.
    """
    # Convert number to string to easily manipulate digits
    s = str(n)
    length = len(s)
    
    # Option 1: The sum of squares of the digits of the original number
    original_sum = sum(int(digit) ** 2 for digit in s)
    
    # Option 2: A number consisting of (length - 1) nines and one leading digit.
    # To maximize the sum of squares, we want the largest possible leading digit.
    # However, the standard greedy approach for "maximizing sum of squares" 
    # via digit manipulation (like in similar problems) is to consider 
    # the number formed by (first_digit - 1) followed by all 9s.
    
    # Let's calculate the sum for the number: (first_digit - 1) followed by (length - 1) nines.
    # This is a common pattern for maximizing digit-based sums.
    first_digit = int(s[0])
    
    # If the first digit is 0 (not possible for positive n), we handle it.
    # If first digit is 1, the leading digit becomes 0, effectively reducing length.
    if first_digit > 0:
        greedy_sum = (first_digit - 1) ** 2 + (length - 1) * (9 ** 2)
    else:
        greedy_sum = 0
        
    # Note: For some variations, we also check the case of all 9s with length-1.
    # But (first_digit - 1) followed by 9s covers the most significant reduction.
    
    # We also need to consider the case where we just use (length - 1) nines.
    # e.g., n = 10 -> length 2. Option 1: 1^2+0^2=1. Option 2: (1-1)^2 + 9^2 = 81? 
    # No, the number must be <= n. If n=10, we can't have 9. 
    # The largest number < 10 is 9. Sum of squares = 81.
    
    # Correct Greedy Strategy for "Max sum of squares of digits of x <= n":
    # 1. Sum of squares of digits of n.
    # 2. For each digit position i, change digit at i to (digit[i] - 1) and all 
    #    subsequent digits to 9.
    
    max_sum = original_sum
    
    # Iterate through each digit position to try the "reduce and fill with 9s" strategy
    for i in range(length):
        digit = int(s[i])
        if digit == 0:
            continue
            
        # Calculate sum: squares of digits before i + (digit-1)^2 + (length - 1 - i) * 9^2
        current_prefix_sum = sum(int(s[j]) ** 2 for j in range(i))
        current_val = current_prefix_sum + (digit - 1) ** 2 + (length - 1 - i) * (9 ** 2)
        
        if current_val > max_sum:
            max_sum = current_val
            
    return max_sum
