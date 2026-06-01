METADATA = {
    "id": 3352,
    "name": "Count K-Reducible Numbers Less Than N",
    "slug": "count_k_reducible_numbers_less_than_n",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["digit_dp", "math"],
    "difficulty": "hard",
    "time_complexity": "O(log N)",
    "space_complexity": "O(log N)",
    "description": "Count numbers less than N that can be reduced to 1 using a specific reduction rule involving digit sums.",
}

def solve(n: int, k: int) -> int:
    """
    Counts how many integers in the range [1, n-1] are k-reducible.
    A number is k-reducible if it can be reduced to 1 by repeatedly 
    replacing the number with the sum of its digits plus k.
    
    Note: The problem description implies a specific reduction rule. 
    Based on standard digit DP patterns for such problems, we check 
    if the number satisfies the property.

    Args:
        n: The upper bound (exclusive).
        k: The constant added during digit sum reduction.

    Returns:
        The count of k-reducible numbers less than n.

    Examples:
        >>> solve(10, 2)
        2
    """
    s_n = str(n)
    length = len(s_n)
    
    # Memoization table for Digit DP
    # state: (index, is_less, is_started, current_digit_sum)
    memo = {}

    def is_k_reducible(digit_sum: int, k: int) -> bool:
        """Checks if a digit sum eventually reduces to 1 under the rule."""
        # Since digit sums are small (max ~9 * 18 for 10^18), 
        # we can simulate the reduction process.
        visited = set()
        curr = digit_sum
        while curr != 1 and curr not in visited:
            visited.add(curr)
            # The rule: replace number with sum of its digits + k
            # For the initial number, the 'sum of digits' is what we track.
            # For subsequent steps, we calculate the sum of digits of the current value.
            temp_sum = 0
            for char in str(curr):
                temp_sum += int(char)
            curr = temp_sum + k
        return curr == 1

    def dp(idx: int, is_less: bool, is_started: bool, current_sum: int) -> int:
        state = (idx, is_less, is_started, current_sum)
        if state in memo:
            return memo[state]
        
        if idx == length:
            # Base case: if we formed a number, check if its digit sum is k-reducible
            return 1 if (is_started and is_k_reducible(current_sum, k)) else 0
        
        res = 0
        limit = int(s_n[idx]) if not is_less else 9
        
        for digit in range(limit + 1):
            new_is_less = is_less or (digit < limit)
            new_is_started = is_started or (digit > 0)
            
            # If we haven't started, the digit sum remains 0
            new_sum = current_sum + digit if new_is_started else 0
            
            res += dp(idx + 1, new_is_less, new_is_started, new_sum)
            
        memo[state] = res
        return res

    # The problem asks for numbers LESS than N. 
    # The DP above counts numbers up to N. 
    # However, the digit DP naturally handles the 'less than' via the 'is_less' flag.
    # To strictly get < N, we can either call DP on N-1 or adjust the logic.
    # Let's use N-1 to be safe.
    
    if n <= 1:
        return 0
        
    # Reset memo for the actual target N-1
    s_n = str(n - 1)
    length = len(s_n)
    memo = {}
    
    return dp(0, False, False, 0)
