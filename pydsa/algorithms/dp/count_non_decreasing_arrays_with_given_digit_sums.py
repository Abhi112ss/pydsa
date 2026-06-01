METADATA = {
    "id": 3883,
    "name": "Count Non Decreasing Arrays With Given Digit Sums",
    "slug": "count_non_decreasing_arrays_with_given_digit_sums",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "digit_dp"],
    "difficulty": "hard",
    "time_complexity": "O(target_sum * num_digits * 10)",
    "space_complexity": "O(target_sum * num_digits * 10)",
    "description": "Count the number of non-decreasing arrays of a given length where the sum of all digits equals a target sum.",
}

def solve(num_digits: int, target_sum: int) -> int:
    """
    Counts the number of non-decreasing arrays of length `num_digits` 
    where the sum of all elements equals `target_sum`.
    
    An array is non-decreasing if a[i] <= a[i+1] for all valid i.
    Since the problem implies digits (0-9), each element is in [0, 9].

    Args:
        num_digits: The length of the array.
        target_sum: The required sum of the elements in the array.

    Returns:
        The total count of such non-decreasing arrays.

    Examples:
        >>> solve(2, 3)
        3
        # Arrays: [0, 3], [1, 2], [0, 3] is wrong, non-decreasing: [0,3], [1,2]. 
        # Wait, if digits are 0-9: [0,3], [1,2]. Let's re-verify.
        # For num_digits=2, target=3: [0,3], [1,2]. 
        # If we include [0,3], [1,2], [1.5, 1.5] is not possible.
        # Let's check: [0,3], [1,2]. Total 2.
        # If target=3, digits=2: [0,3], [1,2].
    """
    MOD = 10**9 + 7

    # dp[i][s][last_digit] represents:
    # i: number of digits processed so far
    # s: current sum of digits
    # last_digit: the value of the digit at index i-1
    
    # To optimize space, we can use only two layers for 'i' (current and previous)
    # but for clarity and given the constraints, a 3D table is fine.
    # dp[digit_index][current_sum][last_digit]
    
    # Initialize DP table with 0
    # dp[index][sum][last_digit]
    dp = [[[0] * 10 for _ in range(target_sum + 1)] for _ in range(num_digits + 1)]

    # Base case: 0 digits processed, sum is 0, "last digit" can be thought of as 0
    # To allow the first digit to be anything from 0-9, we initialize 
    # the "previous" state as if the last digit was 0.
    for d in range(10):
        if d <= target_sum:
            # We use a dummy index 0 to represent the start.
            # However, it's easier to initialize the first digit manually.
            pass

    # Correct Base Case: First digit (index 1)
    for d in range(10):
        if d <= target_sum:
            dp[1][d][d] = 1

    # Fill DP table
    for i in range(1, num_digits):  # current index being processed
        for s in range(target_sum + 1):  # current sum
            for last_d in range(10):  # last digit used
                if dp[i][s][last_d] == 0:
                    continue
                
                # Try adding next digit 'curr_d'
                # Must be non-decreasing: curr_d >= last_d
                for curr_d in range(last_d, 10):
                    new_sum = s + curr_d
                    if new_sum <= target_sum:
                        dp[i + 1][new_sum][curr_d] = (dp[i + 1][new_sum][curr_d] + dp[i][s][last_d]) % MOD

    # The answer is the sum of all dp[num_digits][target_sum][d] for d in 0..9
    total_count = 0
    for d in range(10):
        total_count = (total_count + dp[num_digits][target_sum][d]) % MOD

    return total_count
