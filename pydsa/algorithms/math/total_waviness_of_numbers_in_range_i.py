METADATA = {
    "id": 3751,
    "name": "Total Waviness of Numbers in Range I",
    "slug": "total_waviness_of_numbers_in_range_i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["digit_dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log(n))",
    "space_complexity": "O(log(n))",
    "description": "Count numbers in a range [0, n] where adjacent digits alternate between increasing and decreasing.",
}

def solve(n: int) -> int:
    """
    Calculates the total count of 'wavy' numbers in the range [0, n].
    A number is wavy if the difference between adjacent digits alternates in sign.
    
    Args:
        n: The upper bound of the range (inclusive).

    Returns:
        The count of wavy numbers in [0, n].

    Examples:
        >>> solve(20)
        21  # (Assuming all single digits and specific patterns are wavy)
    """
    s = str(n)
    length = len(s)
    
    # memoization table: (index, last_digit, direction, is_less, is_started, is_second_digit)
    # direction: 0 (none), 1 (increasing: d[i] > d[i-1]), 2 (decreasing: d[i] < d[i-1])
    memo = {}

    def dp(idx: int, last_digit: int, direction: int, is_less: bool, is_started: bool, is_second: bool) -> int:
        state = (idx, last_digit, direction, is_less, is_started, is_second)
        if state in memo:
            return memo[state]
        
        if idx == length:
            return 1 if is_started else 0

        res = 0
        # If we haven't started placing non-zero digits, we can place a 0 and stay 'not started'
        if not is_started:
            res += dp(idx + 1, 0, 0, True, False, True)

        limit = int(s[idx]) if not is_less else 9
        
        # Determine the range of digits we can place at this position
        start_digit = 1 if not is_started else 0
        
        for digit in range(start_digit, limit + 1):
            new_is_less = is_less or (digit < limit)
            
            if not is_started:
                # First non-zero digit placed
                res += dp(idx + 1, digit, 0, new_is_less, True, True)
            elif is_second:
                # Second digit placed: determines the initial direction
                if digit > last_digit:
                    res += dp(idx + 1, digit, 1, new_is_less, True, False)
                elif digit < last_digit:
                    res += dp(idx + 1, digit, 2, new_is_less, True, False)
                # Note: digit == last_digit is not wavy
            else:
                # Subsequent digits: must alternate direction
                if direction == 1: # Previous was increasing, now must decrease
                    if digit < last_digit:
                        res += dp(idx + 1, digit, 2, new_is_less, True, False)
                elif direction == 2: # Previous was decreasing, now must increase
                    if digit > last_digit:
                        res += dp(idx + 1, digit, 1, new_is_less, True, False)
        
        memo[state] = res
        return res

    # The problem asks for range [0, n]. 
    # Single digits (0-9) are technically wavy by vacuous truth or definition.
    # Our DP counts numbers > 0. We add 1 for the number '0'.
    return dp(0, 0, 0, False, False, True) + 1
