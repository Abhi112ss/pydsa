METADATA = {
    "id": 2564,
    "name": "Substring XOR Queries",
    "slug": "substring-xor-queries",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Given an array and queries of ranges, return the XOR sum of each range using prefix XORs.",
}

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the XOR sum for each given range [left, right] in the nums array.

    Args:
        nums: A list of integers.
        queries: A list of queries where each query is [left, right].

    Returns:
        A list of integers representing the XOR sum for each query.

    Examples:
        >>> solve([1, 3, 4, 8], [[0, 3], [1, 2], [0, 1], [3, 3]])
        [14, 7, 2, 8]
    """
    n = len(nums)
    # prefix_xor[i] stores the XOR sum of nums[0...i-1]
    # We use size n + 1 to handle the range [0, right] easily
    prefix_xor = [0] * (n + 1)
    
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ nums[i]
        
    results = []
    for left, right in queries:
        # The XOR sum of range [left, right] is calculated as:
        # (nums[0] ^ ... ^ nums[right]) ^ (nums[0] ^ ... ^ nums[left-1])
        # This cancels out the elements before the 'left' index.
        xor_sum = prefix_xor[right + 1] ^ prefix_xor[left]
        results.append(xor_sum)
        
    return results
