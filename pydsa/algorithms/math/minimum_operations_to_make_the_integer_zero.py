METADATA = {
    "id": 2749,
    "name": "Minimum Operations to Make the Integer Zero",
    "slug": "minimum-operations-to-make-the-integer-zero",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(log(num))",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make an integer zero by subtracting powers of two multiplied by a constant k.",
}

def solve(num: int, num2: int) -> int:
    """
    Calculates the minimum number of operations to make 'num' zero.
    In each operation, we subtract (num2 + 2^i) for some non-negative integer i.

    Args:
        num: The target integer to reduce to zero.
        num2: The constant added to the power of two in each operation.

    Returns:
        The minimum number of operations required, or -1 if impossible.

    Examples:
        >>> solve(5, 3)
        2
        >>> solve(7, 3)
        -1
    """
    # The problem asks to find the minimum k such that:
    # num - k * num2 = sum(2^i_1 + 2^i_2 + ... + 2^i_k)
    # Let target = num - k * num2.
    # For a valid k, target must satisfy:
    # 1. target >= 0 (we can't subtract more than we have)
    # 2. bit_count(target) <= k (we need at least as many powers of 2 as k)
    # 3. target >= k (since each 2^i is at least 2^0 = 1, the sum of k powers is at least k)
    # Note: condition 3 is actually covered by bit_count(target) <= k and target >= 0
    # because if target >= k and we need to represent target using exactly k powers of 2,
    # we can always split a 2^x into 2^(x-1) + 2^(x-1) until we have exactly k terms,
    # provided k <= target.

    # We iterate through possible values of k (number of operations).
    # Since num can be up to 10^9 and num2 can be small, k won't exceed ~60 
    # (the number of bits in a 64-bit integer).
    for k in range(1, 61):
        target = num - (k * num2)
        
        if target < 0:
            # If target becomes negative, increasing k will only make it more negative.
            return -1
        
        # count_set_bits is the minimum number of powers of 2 needed to sum to target.
        # k is the maximum number of powers of 2 we can use (by splitting 2^x into 2^(x-1) + 2^(x-1)).
        # We need: bit_count(target) <= k <= target
        if bin(target).count('1') <= k <= target:
            return k
            
    return -1
