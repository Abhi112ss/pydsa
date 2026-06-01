METADATA = {
    "id": 2343,
    "name": "Query Kth Smallest Trimmed Number",
    "slug": "query-kth-smallest-trimmed-number",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "binary_search", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Given an array of integers, return the k-th smallest number after trimming leading and trailing zeros.",
}

def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    """
    Finds the k-th smallest trimmed number for multiple queries.

    A trimmed number is formed by removing all leading and trailing zeros 
    from the decimal representation of the number.

    Args:
        nums: A list of integers.
        queries: A list of queries where each query is [k, query_index].

    Returns:
        A list of integers representing the k-th smallest trimmed number 
        for each query, or -1 if k is greater than the number of elements.

    Examples:
        >>> solve([10, 2, 30, 4], [[1, 0], [2, 1]])
        [1, 2]
        >>> solve([10, 2, 30, 4], [[5, 0]])
        [-1]
    """
    
    def get_trimmed_value(n: int) -> int:
        """Helper to convert number to string, strip zeros, and return as int."""
        s = str(n).strip('0')
        # If the number was all zeros, strip returns empty string; 
        # however, the problem implies non-zero results or specific handling.
        # Based on constraints, we return 0 if empty.
        return int(s) if s else 0

    # Pre-calculate all trimmed values
    # Time: O(N * average_digits)
    trimmed_nums = []
    for num in nums:
        trimmed_nums.append(get_trimmed_value(num))
    
    # Sort the trimmed values to allow O(1) access for k-th smallest
    # Time: O(N log N)
    trimmed_nums.sort()
    
    results: list[int] = []
    
    # Process each query
    # Time: O(Q)
    for k, query_index in queries:
        # k is 1-indexed in the problem description
        if k <= len(trimmed_nums):
            results.append(trimmed_nums[k - 1])
        else:
            results.append(-1)
            
    return results
