METADATA = {
    "id": 3704,
    "name": "Count No-Zero Pairs That Sum to N",
    "slug": "count-no-zero-pairs-that-sum-to-n",
    "category": "math",
    "aliases": [],
    "tags": ["math", "digit_dp"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Count the number of pairs of positive integers (a, b) such that a + b = n and neither a nor b contains the digit zero.",
}

def solve(n: int) -> int:
    """
    Args:
        n: The target sum.

    Returns:
        The number of pairs (a, b) such that a + b = n and both a and b contain no zero digits.
    """
    digits = []
    temp_n = n
    while temp_n > 0:
        digits.append(temp_n % 10)
        temp_n //= 10
    
    num_digits = len(digits)
    memo = {}

    def count_ways(index: int, carry: int) -> int:
        state = (index, carry)
        if state in memo:
            return memo[state]
        
        if index == num_digits:
            return 1 if carry == 0 else 0
        
        total_ways = 0
        target_digit = digits[index]
        
        for digit_a in range(1, 10):
            for digit_b in range(1, 10):
                current_sum = digit_a + digit_b + carry
                if current_sum % 10 == target_digit:
                    new_carry = current_sum // 10
                    total_ways += count_ways(index + 1, new_carry)
        
        memo[state] = total_ways
        return total_ways

    result = count_ways(0, 0)
    
    if n < 2:
        return 0
        
    return result