METADATA = {
    "id": 3855,
    "name": "Sum of K-Digit Numbers in a Range",
    "slug": "sum_of_k_digit_numbers_in_a_range",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_dp"],
    "difficulty": "medium",
    "time_complexity": "O(log N)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of all k-digit numbers within a given range [low, high].",
}

def solve(low: int, high: int, k: int) -> int:
    """
    Calculates the sum of all k-digit numbers in the range [low, high].

    A k-digit number is defined as a number x such that 10^(k-1) <= x < 10^k.
    The function finds the intersection of the range [low, high] and the 
    range of all k-digit numbers, then applies the arithmetic series sum formula.

    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.
        k (int): The number of digits required.

    Returns:
        int: The sum of all k-digit numbers within [low, high].

    Examples:
        >>> solve(1, 20, 1) # k=1 numbers are 1-9. Range [1, 20] contains 1-9.
        45
        >>> solve(10, 100, 2) # k=2 numbers are 10-99. Range [10, 100] contains 10-99.
        4905
    """
    # Define the boundaries for all k-digit numbers
    # Smallest k-digit number is 10^(k-1), largest is 10^k - 1
    k_digit_min = 10**(k - 1)
    k_digit_max = 10**k - 1

    # Find the intersection of [low, high] and [k_digit_min, k_digit_max]
    # The effective range is [start, end]
    start = max(low, k_digit_min)
    end = min(high, k_digit_max)

    # If the intersection is empty, the sum is 0
    if start > end:
        return 0

    # The numbers in the intersection form an arithmetic progression
    # with a common difference of 1.
    # Sum = (n / 2) * (first_term + last_term)
    # where n is the number of terms: (end - start + 1)
    num_terms = end - start + 1
    
    # Using integer arithmetic to avoid floating point precision issues
    # Sum = (num_terms * (start + end)) // 2
    total_sum = (num_terms * (start + end)) // 2

    return total_sum
