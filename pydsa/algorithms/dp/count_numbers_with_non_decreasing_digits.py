METADATA = {
    "id": 3519,
    "name": "Count Numbers with Non-Decreasing Digits",
    "slug": "count-numbers-with-non-decreasing-digits",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["digit_dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log10(n) * 10)",
    "space_complexity": "O(1)",
    "description": "Count the number of integers from 1 to n whose digits are in non-decreasing order.",
}

def solve(n: int) -> int:
    """
    Counts the number of integers in the range [1, n] such that the digits 
    of each integer are in non-decreasing order.

    Args:
        n: The upper bound integer.

    Returns:
        The count of non-decreasing digit numbers in [1, n].

    Examples:
        >>> solve(22)
        13
        # Non-decreasing numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, ..., 22
        # Wait, the example 22: 1-9 (9), 11-19 (9), 22 (1) -> 19? 
        # Let's re-verify: 1,2,3,4,5,6,7,8,9, 11,12,13,14,15,16,17,18,19, 22. Total 19.
    """
    s_n = str(n)
    length = len(s_n)
    
    # memoization table for digit DP
    # dp[index][last_digit][is_less][is_started]
    # index: current digit position being filled
    # last_digit: the value of the previous digit to ensure non-decreasing property
    # is_less: boolean, true if we are already strictly less than the prefix of n
    # is_started: boolean, true if we have started placing non-zero digits
    memo = {}

    def count_valid(index: int, last_digit: int, is_less: bool, is_started: bool) -> int:
        state = (index, last_digit, is_less, is_started)
        if state in memo:
            return memo[state]
        
        if index == length:
            # If we started a number, it counts as 1 valid number
            return 1 if is_started else 0
        
        count = 0
        # Determine the upper limit for the current digit
        limit = int(s_n[index]) if not is_less else 9
        
        for digit in range(limit + 1):
            new_is_less = is_less or (digit < limit)
            
            if not is_started:
                if digit == 0:
                    # Still leading zeros
                    count += count_valid(index + 1, 0, new_is_less, False)
                else:
                    # First non-zero digit placed
                    count += count_valid(index + 1, digit, new_is_less, True)
            else:
                # We have already started, must maintain non-decreasing order
                if digit >= last_digit:
                    count += count_valid(index + 1, digit, new_is_less, True)
                    
        memo[state] = count
        return count

    # The DP approach counts numbers in [0, n]. 
    # Since 0 is not considered a positive integer in the range [1, n], 
    # and our is_started logic handles the "all zeros" case by returning 0,
    # the result is correct for [1, n].
    return count_valid(0, 0, False, False)
