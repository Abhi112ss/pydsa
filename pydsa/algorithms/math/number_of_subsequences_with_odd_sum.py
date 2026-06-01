METADATA = {
    "id": 3247,
    "name": "Number of Subsequences with Odd Sum",
    "slug": "number_of_subsequences_with_odd_sum",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of non-empty subsequences of an array that have an odd sum, modulo 10^9 + 7.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of non-empty subsequences with an odd sum.

    A subsequence has an odd sum if and only if it contains an odd number 
    of odd elements. The number of even elements included does not affect 
    the parity of the sum.

    Args:
        nums: A list of integers.

    Returns:
        The number of subsequences with an odd sum modulo 10^9 + 7.

    Examples:
        >>> solve([1, 3, 5])
        4
        >>> solve([2, 4, 6])
        0
        >>> solve([1, 2, 3])
        4
    """
    MOD = 10**9 + 7
    
    odd_count = 0
    even_count = 0
    
    for num in nums:
        if num % 2 == 1:
            odd_count += 1
        else:
            even_count += 1
            
    if odd_count == 0:
        return 0

    # Combinatorics logic:
    # 1. To get an odd sum, we must pick an odd number of elements from the 'odd_count' set.
    #    The number of ways to pick an odd number of elements from a set of size N is 2^(N-1).
    # 2. We can pick any number of elements from the 'even_count' set.
    #    The number of ways to pick any subset from a set of size M is 2^M.
    # Total ways = 2^(odd_count - 1) * 2^(even_count) = 2^(odd_count + even_count - 1)
    # Since odd_count + even_count = len(nums), the result is 2^(len(nums) - 1).
    
    # However, the problem asks for non-empty subsequences. 
    # The formula 2^(odd_count - 1) * 2^(even_count) already accounts for the 
    # requirement of having at least one odd element, so the subsequence is 
    # guaranteed to be non-empty.
    
    # Using modular exponentiation for efficiency and to handle large powers.
    # Result = (2^(odd_count - 1) % MOD) * (2^even_count % MOD) % MOD
    
    # Simplified: 2^(total_elements - 1) % MOD
    # This works because if odd_count > 0, there is always at least one way 
    # to pick an odd number of odd elements.
    
    return pow(2, len(nums) - 1, MOD)
