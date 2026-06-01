METADATA = {
    "id": 3870,
    "name": "Count Commas in Range",
    "slug": "count_commas_in_range",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of commas used when writing all integers in the range [low, high] in standard decimal notation.",
}

def solve(low: int, high: int) -> int:
    """
    Calculates the total number of commas used to format all integers from low to high.
    
    A comma is placed every three digits starting from the right (e.g., 1,000, 1,000,000).
    The number of commas in an integer x is floor(log10(x) / 3) if x > 0, else 0.
    However, a more robust way is to count how many numbers have at least 4 digits, 
    at least 7 digits, etc.

    Args:
        low: The starting integer of the range (inclusive).
        high: The ending integer of the range (inclusive).

    Returns:
        The total count of commas used for all numbers in the range.

    Examples:
        >>> solve(1, 10)
        0
        >>> solve(1, 1000)
        1
        >>> solve(999, 1001)
        2  # 999 (0), 1000 (1), 1001 (1)
    """
    
    def count_commas_up_to(n: int) -> int:
        """
        Helper to count total commas for all numbers from 1 to n.
        
        A number has at least 1 comma if it is >= 1,000.
        A number has at least 2 commas if it is >= 1,000,000.
        A number has at least k commas if it is >= 10^(3k).
        """
        if n < 1000:
            return 0
        
        total_commas = 0
        # A number x has floor(log10(x)/3) commas if we consider the 
        # standard grouping. More simply:
        # Every number in [10^3, 10^4 - 1] has 1 comma.
        # Every number in [10^6, 10^7 - 1] has 2 commas.
        # We can sum the counts of numbers that reach each threshold.
        
        threshold = 1000
        while threshold <= n:
            # Count how many numbers in [1, n] are >= threshold
            # and specifically contribute an additional comma at this magnitude.
            # Actually, it's simpler: 
            # Total commas = (count of numbers >= 1,000) + (count of numbers >= 1,000,000) + ...
            total_commas += (n - threshold + 1)
            threshold *= 1000
            
        return total_commas

    # The total commas in [low, high] is the total up to high minus total up to (low - 1)
    return count_commas_up_to(high) - count_commas_up_to(low - 1)
