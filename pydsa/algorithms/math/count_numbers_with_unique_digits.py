METADATA = {
    "id": 357,
    "name": "Count Numbers with Unique Digits",
    "slug": "count-numbers-with-unique-digits",
    "category": "math",
    "aliases": [],
    "tags": ["combinatorics", "math", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given an integer n, return the count of numbers less than 10^n with unique digits.",
}

def solve(n: int) -> int:
    """
    Calculates the count of numbers less than 10^n that have unique digits.

    The problem is solved using combinatorics. 
    - For n=0, the only number is 0 (10^0 = 1, numbers < 1 are just 0).
    - For n=1, numbers are 0-9 (10 total).
    - For n > 1, we calculate the count for each specific digit length k (from 1 to n) 
      and sum them up.
    - For a number of length k:
        - The first digit has 9 choices (1-9, cannot be 0).
        - The second digit has 9 choices (0-9, excluding the first digit).
        - The third digit has 8 choices, and so on.

    Args:
        n: The exponent such that we consider numbers in the range [0, 10^n).

    Returns:
        The total count of numbers less than 10^n with unique digits.

    Examples:
        >>> solve(0)
        1
        >>> solve(1)
        10
        >>> solve(2)
        91
    """
    if n == 0:
        return 1
    
    # Base case: for n=1, numbers are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (total 10)
    total_count = 10
    
    # If n > 10, any number with more than 10 digits must have repeating digits.
    # However, the problem asks for numbers < 10^n. 
    # Since we only have 10 unique digits, we cap n at 10 for the loop.
    limit = min(n, 10)
    
    # current_unique_permutations tracks how many unique numbers exist for a specific length 'k'
    # For k=2: 9 (choices for 1st digit) * 9 (choices for 2nd digit)
    # For k=3: 9 * 9 * 8
    current_unique_permutations = 9
    available_choices = 9
    
    for k in range(2, limit + 1):
        # Calculate permutations for length k
        # Each step we multiply by the remaining available digits
        current_unique_permutations *= available_choices
        total_count += current_unique_permutations
        available_choices -= 1
        
    return total_count
