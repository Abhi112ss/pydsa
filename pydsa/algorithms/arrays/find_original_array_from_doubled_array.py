METADATA = {
    "id": 2007,
    "name": "Find Original Array From Doubled Array",
    "slug": "find-original-array-from-doubled-array",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given a doubled array, reconstruct the original array by greedily matching elements with their doubles.",
}

from collections import Counter

def solve(arr: list[int]) -> list[int]:
    """
    Reconstructs the original array from a doubled array.

    A doubled array is an array where every element x from the original array 
    is paired with 2*x.

    Args:
        arr: A list of integers representing the doubled array.

    Returns:
        A list of integers representing the original array if it exists, 
        otherwise an empty list.

    Examples:
        >>> solve([1, 3, 4, 2, 6, 8])
        [1, 3, 4]
        >>> solve([1, 2, 3, 4, 5, 6])
        []
        >>> solve([0, 0, 0, 0])
        [0, 0]
    """
    # If the length is odd, it's impossible to have pairs
    if len(arr) % 2 != 0:
        return []

    # Count frequencies of all numbers to allow O(1) lookup and updates
    counts = Counter(arr)
    
    # Sort the unique elements to process smaller numbers first.
    # This ensures that when we encounter x, we look for 2x, 
    # rather than accidentally treating 2x as the 'original' for 4x.
    # We sort by absolute value to handle negative numbers correctly (e.g., -2 should match -4).
    sorted_keys = sorted(counts.keys(), key=abs)
    
    original_array = []

    for num in sorted_keys:
        # If we have more of 'num' than available, it's an invalid doubled array
        if counts[num] > counts.get(2 * num, 0) if num != 0 else counts[num] % 2 != 0:
            # Special case for 0: it must appear an even number of times
            if num == 0 and counts[num] % 2 != 0:
                return []
            # For non-zero: if we need more 2*num than we have, it's invalid
            if num != 0 and counts[num] > counts[2 * num]:
                return []

        # If num is 0, we can only pair it with itself
        if num == 0:
            if counts[num] % 2 != 0:
                return []
            # Add half of the zeros to the original array
            original_array.extend([0] * (counts[num] // 2))
            counts[0] = 0
        else:
            # For each instance of 'num', we must find a corresponding '2 * num'
            # We use the count of 'num' to determine how many pairs to form
            num_count = counts[num]
            if num_count > 0:
                # Check if there are enough doubles available
                if counts[2 * num] < num_count:
                    return []
                
                # Add 'num' to the result and consume the '2 * num' from the map
                original_array.extend([num] * num_count)
                counts[2 * num] -= num_count
                counts[num] = 0

    # If the original array doesn't have exactly half the elements, it's invalid
    if len(original_array) != len(arr) // 2:
        return []

    return original_array
