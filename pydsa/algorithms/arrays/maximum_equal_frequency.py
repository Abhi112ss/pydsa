METADATA = {
    "id": 1224,
    "name": "Maximum Equal Frequency",
    "slug": "maximum-equal-frequency",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if it is possible to make all elements in an array have equal frequency by removing exactly one element.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if removing exactly one element from the array can result in all 
    remaining elements having the same frequency.

    Args:
        nums: A list of integers.

    Returns:
        True if a valid element can be removed to make all frequencies equal, 
        False otherwise.

    Examples:
        >>> solve([2, 2, 2, 2])
        True
        >>> solve([1, 2, 2, 2, 2])
        True
        >>> solve([1, 2, 2, 2, 3])
        False
    """
    if not nums:
        return False

    # count_map: maps element -> its frequency
    # freq_map: maps frequency -> how many elements have that frequency
    count_map = {}
    freq_map = {}
    
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1
        
    for count in count_map.values():
        freq_map[count] = freq_map.get(count, 0) + 1

    # n is the total number of elements
    # m is the number of unique elements
    n = len(nums)
    m = len(count_map)

    # Case 1: All elements are the same (e.g., [1, 1, 1])
    # Removing one element leaves all remaining elements with the same frequency.
    if len(freq_map) == 1:
        # If there's only one unique element, we can always remove one.
        # If there are multiple unique elements but they all have the same frequency,
        # we can only remove one if that frequency is 1 (e.g., [1, 2, 3] -> [1, 2]).
        # Wait, if freq_map has 1 key, say {3: 1}, it means all elements have freq 3.
        # If m > 1, removing one element changes the frequency of one element, 
        # breaking the equality unless that frequency was 1.
        # Actually, if m == 1, it's always True.
        # If m > 1 and freq is 1, it's True (e.g., [1, 2, 3] -> [1, 2]).
        # If m > 1 and freq > 1, it's False (e.g., [1, 1, 2, 2] -> [1, 1, 2]).
        single_freq = list(freq_map.keys())[0]
        return m == 1 or single_freq == 1

    # Case 2: There are exactly two different frequencies present.
    if len(freq_map) == 2:
        # Sort frequencies to identify the smaller (f1) and larger (f2)
        f_list = sorted(freq_map.keys())
        f1, f2 = f_list[0], f_list[1]
        count1, count2 = freq_map[f1], freq_map[f2]

        # Condition A: The smaller frequency is 1 and there is only one element with that frequency.
        # This means we can remove that single element (e.g., [1, 2, 2, 2] -> f1=1, f2=3).
        if f1 == 1 and count1 == 1:
            return True
        
        # Condition B: The larger frequency is exactly 1 greater than the smaller frequency,
        # and there is only one element with that larger frequency.
        # This means we can reduce that one element's frequency by 1 to match the others.
        # (e.g., [1, 1, 2, 2, 3, 3, 3] -> f1=2, f2=3, count2=1. Remove one '3' -> all freq 2).
        if f2 == f1 + 1 and count2 == 1:
            return True

    return False
