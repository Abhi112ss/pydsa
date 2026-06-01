METADATA = {
    "id": 1310,
    "name": "XOR Queries of a Subarray",
    "slug": "xor-queries-of-a-subarray",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Given an array and multiple queries, return the XOR sum of elements in the specified ranges using prefix XORs.",
}

def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the XOR sum for each query range [left, right] in the given array.

    Args:
        arr: A list of integers.
        queries: A list of queries, where each query is a list [left, right].

    Returns:
        A list of integers representing the XOR sum for each query.

    Examples:
        >>> solve([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]])
        [2, 7, 14, 8]
    """
    n = len(arr)
    
    # Precompute prefix XOR array.
    # prefix_xor[i] stores the XOR sum of arr[0...i-1].
    # prefix_xor[0] is initialized to 0 to handle the base case.
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

    results = []
    for left, right in queries:
        # The XOR sum of range [left, right] is calculated using the property:
        # XOR(L, R) = prefix_xor[R + 1] ^ prefix_xor[L]
        # This works because (arr[0]^...^arr[R]) ^ (arr[0]^...^arr[L-1]) 
        # cancels out the elements from index 0 to L-1.
        query_result = prefix_xor[right + 1] ^ prefix_xor[left]
        results.append(query_result)

    return results
