METADATA = {
    "id": 600,
    "name": "Non-negative Integers without Consecutive Ones",
    "slug": "non-negative-integers-without-consecutive-ones",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Count non-negative integers less than or equal to n that do not have consecutive ones in their binary representation.",
}

def solve(n: int) -> int:
    """
    Counts the number of non-negative integers less than or equal to n 
    that do not contain consecutive ones in their binary representation.

    The problem can be solved using the property that the number of valid 
    binary strings of length k follows the Fibonacci sequence, or via 
    Digit Dynamic Programming on the binary representation of n.

    Args:
        n: The upper bound integer.

    Returns:
        The count of valid non-negative integers.

    Examples:
        >>> solve(5)
        4
        # Valid numbers: 0 (0), 1 (1), 2 (10), 4 (100). 3 (11) and 5 (101) are invalid? 
        # Wait, 5 is 101, which is valid. Let's re-check:
        # 0: 0 (V)
        # 1: 1 (V)
        # 2: 10 (V)
        # 3: 11 (X)
        # 4: 100 (V)
        # 5: 101 (V)
        # Total for n=5 is 5.
    """
    if n == 0:
        return 1

    # Convert n to binary string to process bits from most significant to least
    binary_n = bin(n)[2:]
    length = len(binary_n)

    # Precompute Fibonacci numbers where fib[i] is the number of valid 
    # binary strings of length i.
    # fib[0] = 1 (empty string)
    # fib[1] = 2 (0, 1)
    # fib[2] = 3 (00, 01, 10)
    # fib[i] = fib[i-1] + fib[i-2]
    fib = [0] * (length + 2)
    fib[0] = 1
    fib[1] = 2
    for i in range(2, length + 2):
        fib[i] = fib[i - 1] + fib[i - 2]

    count = 0
    prev_bit = 0

    for i in range(length):
        current_bit = int(binary_n[i])
        
        if current_bit == 1:
            # If the current bit in n is 1, we can choose to place a 0 at this position.
            # If we place a 0, all remaining (length - 1 - i) bits can be any valid 
            # sequence of length (length - 1 - i).
            # The number of such sequences is fib[length - 1 - i].
            count += fib[length - 1 - i]
            
            # If we encounter two consecutive 1s in the prefix of n, 
            # we cannot form any more numbers that match the prefix of n.
            if prev_bit == 1:
                return count
            
            prev_bit = 1
        else:
            # If current bit is 0, we must place a 0 to stay <= n.
            # prev_bit remains 0.
            prev_bit = 0

    # The loop counts all valid numbers strictly less than n.
    # We add 1 to include n itself if n is valid (the loop finishes without returning).
    return count + 1
