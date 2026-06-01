METADATA = {
    "id": 954,
    "name": "Array of Doubled Pairs",
    "slug": "array-of-doubled-pairs",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be rearranged into pairs where each pair consists of an element and its double.",
}

from collections import Counter

def solve(arr: list[int]) -> bool:
    """
    Determines if the array can be rearranged into pairs (x, 2x).

    The algorithm sorts the array by absolute values to ensure that when we 
    process an element 'x', its potential partner '2x' has not been 
    processed yet (unless x is 0). We then use a frequency map to greedily 
    match elements.

    Args:
        arr: A list of integers.

    Returns:
        True if the array can be partitioned into doubled pairs, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4])
        True
        >>> solve([1, 2, 3, 4, 5, 6])
        False
        >>> solve([4, -2, 2, -4])
        True
    """
    if len(arr) % 2 != 0:
        return False

    # Count frequencies of each number
    counts = Counter(arr)
    
    # Sort elements by their absolute value.
    # This is crucial because for any x, we want to find 2x.
    # By sorting by abs(x), we ensure that we always look for the 'larger' 
    # magnitude partner after processing the 'smaller' magnitude element.
    sorted_keys = sorted(counts.keys(), key=abs)

    for x in sorted_keys:
        # If we have more of x than we can match, it's impossible
        if counts[x] > counts[2 * x] if x != 0 else counts[x] % 2 != 0:
            # Special case for 0: they must come in even pairs
            if x == 0:
                if counts[x] % 2 != 0:
                    return False
            else:
                return False
        
        # If x is 0, we've already checked parity, just reduce count
        if x == 0:
            counts[x] = 0
        else:
            # Greedily consume the required number of 2*x elements
            # to satisfy the current count of x
            needed_partners = counts[x]
            if counts[2 * x] < needed_partners:
                return False
            counts[2 * x] -= needed_partners
            counts[x] = 0

    return True
