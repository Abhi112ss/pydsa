METADATA = {
    "id": 1566,
    "name": "Detect Pattern of Length M Repeated K or More Times",
    "slug": "detect-pattern-of-length-m-repeated-k-or-more-times",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Determine if there exists a pattern of length m that repeats consecutively k or more times in the given array.",
}

def solve(arr: list[int], m: int, k: int) -> bool:
    """
    Determines if there is a pattern of length m that repeats k or more times consecutively.

    Args:
        arr: The input list of integers.
        m: The length of the pattern to look for.
        k: The minimum number of consecutive repetitions required.

    Returns:
        True if such a pattern exists, False otherwise.

    Examples:
        >>> solve([1, 2, 1, 2, 1, 2, 3], 2, 3)
        True
        >>> solve([1, 2, 3, 4, 5], 2, 2)
        False
    """
    n = len(arr)
    # A pattern of length m repeated k times requires at least m * k elements
    if n < m * k:
        return False

    # Iterate through every possible starting position of a pattern
    # We only need to check up to the point where k repetitions can still fit
    for start_index in range(n - m * k + 1):
        # Define the candidate pattern based on the current starting index
        pattern = arr[start_index : start_index + m]
        
        count = 1
        current_pos = start_index + m
        
        # Check how many times this specific pattern repeats consecutively
        while current_pos + m <= n:
            # Compare the next segment of length m with our candidate pattern
            is_match = True
            for i in range(m):
                if arr[current_pos + i] != pattern[i]:
                    is_match = False
                    break
            
            if is_match:
                count += 1
                current_pos += m
                # If we reached the required k repetitions, return True immediately
                if count >= k:
                    return True
            else:
                # Pattern sequence broken, stop checking this start_index
                break
                
    return False
