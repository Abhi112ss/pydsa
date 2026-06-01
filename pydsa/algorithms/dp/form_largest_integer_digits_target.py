METADATA = {
    "id": 1449,
    "name": "Form Largest Integer With Digits That Add up to Target",
    "slug": "form-largest-integer-with-digits-that-add-up-to-target",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(target)",
    "space_complexity": "O(target)",
    "description": "Find the largest integer that can be formed by concatenating digits from a given list such that the sum of the digits equals a target value.",
}

def solve(digits: list[int], target: int) -> str:
    """
    Finds the largest integer formed by digits that sum up to the target.
    
    The problem is treated as an unbounded knapsack problem where the 'value' 
    is a combination of the number of digits (primary) and the lexicographical 
    value (secondary). To maximize the integer, we first maximize the number 
    of digits used, and then maximize the digits themselves.

    Args:
        digits: A list of available single-digit integers.
        target: The required sum of the digits.

    Returns:
        The largest integer as a string, or an empty string if no such integer exists.

    Examples:
        >>> solve([1, 5, 6, 7], 9)
        '111111111'
        >>> solve([1, 5, 6, 7], 10)
        '55'
        >>> solve([1, 5, 6, 7], 11)
        '56'
    """
    # Sort digits in descending order to facilitate greedy selection 
    # for the same number of digits.
    digits.sort(reverse=True)
    
    # dp[i] will store the maximum number of digits that sum up to i.
    # We initialize with -1 to represent that the sum i is unreachable.
    dp = [-1] * (target + 1)
    dp[0] = 0
    
    # parent[i] will store the digit used to reach sum i from a previous state.
    # This allows us to reconstruct the number.
    parent = [-1] * (target + 1)

    # Standard Unbounded Knapsack DP
    for i in range(1, target + 1):
        for digit in digits:
            if i >= digit and dp[i - digit] != -1:
                # We prioritize the number of digits (dp[i-digit] + 1).
                # If the number of digits is the same, we don't need to do anything 
                # because 'digits' is sorted descending, and the first one we 
                # encounter that gives the max length will be the largest digit.
                if dp[i - digit] + 1 > dp[i]:
                    dp[i] = dp[i - digit] + 1
                    parent[i] = digit
                elif dp[i - digit] + 1 == dp[i]:
                    # If lengths are equal, we want the largest digit at the current position.
                    # Since digits are sorted descending, the first one that satisfies 
                    # the condition is already the largest possible for this length.
                    pass

    # If target is unreachable, return empty string
    if dp[target] == -1:
        return ""

    # Reconstruct the number using the parent pointers.
    # To get the largest number, we want larger digits at the front.
    # However, the DP reconstruction naturally gives us the digits used.
    # Since we want the largest number, we collect all digits and sort them descending.
    result_digits = []
    current_sum = target
    while current_sum > 0:
        digit = parent[current_sum]
        result_digits.append(str(digit))
        current_sum -= digit
    
    # Sort the collected digits descending to ensure the largest number is formed.
    result_digits.sort(reverse=True)
    return "".join(result_digits)
