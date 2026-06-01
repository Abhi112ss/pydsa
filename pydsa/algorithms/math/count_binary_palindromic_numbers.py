METADATA = {
    "id": 3677,
    "name": "Count Binary Palindromic Numbers",
    "slug": "count-binary-palindromic-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Count the number of integers in the range [1, n] whose binary representation is a palindrome.",
}

def solve(n: int) -> int:
    """
    Counts the number of integers in the range [1, n] whose binary representation is a palindrome.

    The algorithm iterates through possible bit lengths from 1 up to the bit length of n.
    For each length, it calculates how many palindromes exist. If the length is less than 
    the bit length of n, all possible palindromes of that length are counted. 
    If the length equals the bit length of n, it counts only those palindromes <= n.

    Args:
        n: The upper bound of the range [1, n].

    Returns:
        The count of binary palindromic numbers in the range [1, n].

    Examples:
        >>> solve(5) # Binary: 1(1), 3(11), 5(101)
        3
        >>> solve(10) # Binary: 1(1), 3(11), 5(101), 7(111), 9(1001)
        5
    """
    if n <= 0:
        return 0

    def count_palindromes_of_length(length: int, limit: int | None = None) -> int:
        """
        Counts palindromes of a specific bit length.
        If limit is provided, counts palindromes <= limit.
        """
        if length == 0:
            return 0
        
        # A palindrome of length L is determined by its first ceil(L/2) bits.
        # The first bit must be 1 (to maintain length).
        half_len = (length + 1) // 2
        
        # Smallest possible prefix for this length (e.g., for length 5, half_len is 3, prefix starts at 100 binary = 4)
        min_prefix = 1 << (half_len - 1)
        # Largest possible prefix (e.g., for length 5, half_len is 3, prefix ends at 111 binary = 7)
        max_prefix = (1 << half_len) - 1

        if limit is None:
            # Total palindromes of this length is the number of valid prefixes
            return max_prefix - min_prefix + 1
        
        # If we have a limit, we need to find how many prefixes result in a palindrome <= limit
        # First, find the prefix of the limit itself
        limit_bin = bin(limit)[2:]
        if len(limit_bin) > length:
            # If limit is larger than any number of this length, all are valid
            return max_prefix - min_prefix + 1
        if len(limit_bin) < length:
            # If limit is smaller than any number of this length, none are valid
            return 0

        # Extract the prefix of the limit
        limit_prefix = int(limit_bin[:half_len], 2)
        
        # Check if the palindrome formed by limit_prefix is actually <= limit
        # Construct the full palindrome from the prefix
        s_prefix = limit_bin[:half_len]
        if length % 2 == 0:
            # Even length: prefix + reversed prefix
            p_str = s_prefix + s_prefix[::-1]
        else:
            # Odd length: prefix + reversed prefix (excluding the middle bit)
            p_str = s_prefix + s_prefix[:-1][::-1]
        
        palindrome_from_limit = int(p_str, 2)
        
        if palindrome_from_limit <= limit:
            # The limit_prefix itself is valid
            return limit_prefix - min_prefix + 1
        else:
            # The limit_prefix forms a palindrome too large, so we take up to limit_prefix - 1
            return limit_prefix - min_prefix

    total_count = 0
    n_bit_len = n.bit_length()

    # 1. Count all palindromes for all bit lengths strictly less than n's bit length
    for length in range(1, n_bit_len):
        total_count += count_palindromes_of_length(length)

    # 2. Count palindromes of exactly n's bit length that are <= n
    total_count += count_palindromes_of_length(n_bit_len, n)

    return total_count
