METADATA = {
    "id": 1416,
    "name": "Restore The Array",
    "slug": "restore_the_array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given an array of differences, reconstruct the original array if possible.",
}

def solve(differences: list[int]) -> list[int]:
    """
    Reconstructs the original array from a list of differences between adjacent elements.

    The algorithm uses a greedy approach: the smallest difference must exist between 
    the minimum element and its neighbor. By sorting the differences, we can 
    iteratively place the smallest remaining difference to find the next element.

    Args:
        differences: A list of integers representing the absolute differences 
            between adjacent elements in the original array.

    Returns:
        A list of integers representing the original array, or an empty list 
            if no such array exists.

    Examples:
        >>> solve([1, 2, 1])
        [1, 2, 4, 3]
        >>> solve([1, 1, 1])
        []
    """
    n = len(differences)
    # The original array will have n + 1 elements
    target_size = n + 1
    
    # Sort differences to always pick the smallest gap first
    sorted_diffs = sorted(differences)
    
    # We use a frequency map to keep track of available differences
    # This allows O(1) lookup and removal
    diff_counts = {}
    for d in sorted_diffs:
        diff_counts[d] = diff_counts.get(d, 0) + 1
        
    # Start with the smallest possible value (1)
    # We will build the array by greedily adding the smallest available difference
    result = [1]
    
    for _ in range(n):
        # Find the smallest difference that is still available
        # Since sorted_diffs is sorted, we can iterate through it
        found = False
        for d in sorted_diffs:
            if diff_counts.get(d, 0) > 0:
                # Try adding the difference to the last element
                next_val = result[-1] + d
                result.append(next_val)
                diff_counts[d] -= 1
                found = True
                break
        
        if not found:
            return []

    # Validation Step:
    # The greedy construction only ensures we used all differences.
    # We must verify if the resulting array actually produces the input differences.
    # Note: The problem implies the array is a sequence, but the differences 
    # provided are between adjacent elements in the original order.
    # However, the problem asks to restore 'the' array, implying the differences 
    # are the absolute differences |a[i] - a[i+1]|.
    
    # Re-calculate differences from our constructed array
    actual_diffs = []
    for i in range(len(result) - 1):
        actual_diffs.append(abs(result[i] - result[i+1]))
    
    # Check if the sorted actual differences match the sorted input differences
    if sorted(actual_diffs) == sorted_diffs:
        return result
    
    return []
