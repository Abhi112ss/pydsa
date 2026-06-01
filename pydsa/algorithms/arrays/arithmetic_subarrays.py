METADATA = {
    "id": 1630,
    "name": "Arithmetic Subarrays",
    "slug": "arithmetic_subarrays",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(m * n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if given subarrays can be rearranged to form an arithmetic progression.",
}

def solve(nums: list[int], queries: list[list[int]]) -> list[bool]:
    """
    Determines if each subarray defined by queries can be rearranged into an arithmetic sequence.

    An arithmetic sequence is a sequence where the difference between any two 
    consecutive elements is the same.

    Args:
        nums: A list of integers.
        queries: A list of queries, where each query is [start, end] representing 
                 the inclusive range of the subarray.

    Returns:
        A list of booleans where the i-th element is True if the i-th query 
        subarray can form an arithmetic sequence, and False otherwise.

    Examples:
        >>> solve([4, 6, 5, 9, 3, 7], [[0, 2], [0, 3], [2, 5], [1, 3]])
        [True, False, True, True]
    """
    results = []

    for start, end in queries:
        # Extract the subarray defined by the query range
        subarray = nums[start : end + 1]
        
        # A sequence with fewer than 2 elements is technically arithmetic,
        # but based on problem constraints, subarrays will have at least 2 elements.
        if len(subarray) < 2:
            results.append(True)
            continue

        # Sort the subarray to check for constant difference between consecutive elements
        subarray.sort()
        
        # Calculate the common difference from the first two elements
        diff = subarray[1] - subarray[0]
        is_arithmetic = True
        
        # Verify if every consecutive pair maintains the same difference
        for i in range(2, len(subarray)):
            if subarray[i] - subarray[i - 1] != diff:
                is_arithmetic = False
                break
        
        results.append(is_arithmetic)

    return results
