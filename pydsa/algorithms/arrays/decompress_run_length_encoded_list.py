METADATA = {
    "id": 1313,
    "name": "Decompress Run-Length Encoded List",
    "slug": "decompress-run-length-encoded-list",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Decompress a run-length encoded list where every two consecutive integers represent a frequency and a value.",
}

def solve(arr: list[int]) -> list[int]:
    """
    Decompresses a run-length encoded list.

    The input list `arr` is structured such that for every pair of elements 
    (arr[i], arr[i+1]), arr[i] is the frequency and arr[i+1] is the value.

    Args:
        arr: A list of integers representing the encoded sequence.

    Returns:
        A list of integers representing the decompressed sequence.

    Examples:
        >>> solve([1, 2, 3, 4])
        [2, 4, 4, 4]
        >>> solve([3, 1])
        [1, 1, 1]
    """
    decompressed_result: list[int] = []
    
    # Iterate through the array in steps of 2 to process pairs (freq, val)
    for i in range(0, len(arr), 2):
        frequency = arr[i]
        value = arr[i + 1]
        
        # Extend the result list by repeating the value 'frequency' times
        # This is more efficient than a nested loop with append()
        decompressed_result.extend([value] * frequency)
        
    return decompressed_result
