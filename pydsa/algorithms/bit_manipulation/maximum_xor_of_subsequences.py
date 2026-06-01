METADATA = {
    "id": 3681,
    "name": "Maximum XOR of Subsequences",
    "slug": "maximum_xor_of_subsequences",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["linear_basis", "bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(log(max_val))",
    "description": "Find the maximum possible XOR sum of any subsequence of a given array using a linear basis.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum XOR sum possible from any subsequence of the input array.

    This implementation uses the Linear Basis technique. A linear basis is a 
    minimal set of numbers that can represent the XOR sum of any subsequence 
    of the original array. By constructing this basis, we can greedily 
    build the maximum XOR value.

    Args:
        nums: A list of integers.

    Returns:
        The maximum XOR sum achievable by any subsequence.

    Examples:
        >>> solve([3, 10, 5, 25, 2, 8])
        28
        >>> solve([1, 2, 3, 4, 5])
        7
    """
    # The basis will store numbers where the highest set bit is unique for each index.
    # Since integers are typically up to 32 or 64 bits, a size of 64 is safe.
    basis: list[int] = [0] * 64

    for num in nums:
        # Attempt to insert each number into the linear basis
        for i in range(63, -1, -1):
            # If the i-th bit is not set, this bit cannot contribute to the basis at this level
            if not (num >> i) & 1:
                continue

            if not basis[i]:
                # If no basis element exists for this bit position, insert it
                basis[i] = num
                break
            
            # If a basis element already exists, XOR the number to eliminate the i-th bit
            # and continue checking lower bits
            num ^= basis[i]

    # Greedily construct the maximum XOR sum
    max_xor = 0
    for i in range(63, -1, -1):
        # If XORing the current basis element increases the total, include it
        # This works because basis[i] is guaranteed to have its highest bit at position i
        if (max_xor ^ basis[i]) > max_xor:
            max_xor ^= basis[i]

    return max_xor
