METADATA = {
    "id": 3871,
    "name": "Count Commas in Range II",
    "slug": "count_commas_in_range_ii",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_dp"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(log10(n))",
    "description": "Count the total number of commas used in the standard decimal representation of all integers in the range [L, R].",
}

def solve(L: int, R: int) -> int:
    """
    Calculates the total number of commas used in the standard decimal representation 
    of all integers in the range [L, R].

    A comma is placed every three digits from the right (e.g., 1,000,000).
    The number of commas in a number 'n' is max(0, floor(log10(n)/3) - (if n is power of 10...)).
    More simply, a number 'n' has a comma at position 'k' (from right, 0-indexed) 
    if the digit at that position is part of a group of 3.
    Actually, the number of commas in 'n' is simply:
    If n < 1000, 0 commas.
    If 1000 <= n < 1,000,000, 1 comma.
    If 1,000,000 <= n < 1,000,000,000, 2 commas.
    In general, for a number with 'd' digits, the number of commas is max(0, d - 1 - (d-1)%3 - (1 if d%3==1 else 0) ... wait.
    Let's use the rule: a number with 'd' digits has floor((d-1)/3) commas.
    Example: 
    d=1 (1): floor(0/3) = 0
    d=3 (100): floor(2/3) = 0
    d=4 (1000): floor(3/3) = 1
    d=6 (100000): floor(5/3) = 1
    d=7 (1000000): floor(6/3) = 2

    Args:
        L: The lower bound of the range (inclusive).
        R: The upper bound of the range (inclusive).

    Returns:
        The total count of commas for all integers in [L, R].

    Examples:
        >>> solve(1, 1000)
        1
        >>> solve(999, 1001)
        2
    """

    def count_commas_up_to(n: int) -> int:
        """
        Counts total commas in range [1, n] using the property that 
        the number of commas depends only on the number of digits.
        """
        if n <= 0:
            return 0
        
        s_n = str(n)
        num_digits = len(s_n)
        total_commas = 0
        
        # 1. Count commas for all numbers with fewer digits than 'n'
        # For a fixed number of digits 'd', every number has floor((d-1)/3) commas.
        for d in range(1, num_digits):
            # Count of numbers with exactly 'd' digits: 9 * 10^(d-1)
            count_of_numbers = 9 * (10 ** (d - 1))
            commas_per_number = (d - 1) // 3
            total_commas += count_of_numbers * commas_per_number
            
        # 2. Count commas for numbers with exactly 'num_digits' digits up to 'n'
        # All these numbers have the same number of commas: (num_digits - 1) // 3
        commas_per_number_current = (num_digits - 1) // 3
        # Count of numbers from 10^(num_digits-1) to n
        count_of_numbers_current = n - (10 ** (num_digits - 1)) + 1
        total_commas += count_of_numbers_current * commas_per_number_current
        
        return total_commas

    # The result for [L, R] is the result for [1, R] minus the result for [1, L-1]
    return count_commas_up_to(R) - count_commas_up_to(L - 1)
