METADATA = {
    "id": 2300,
    "name": "Successful Pairs of Spells and Potions",
    "slug": "successful_pairs_of_spells_and_potions",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O((n + m) log m)",
    "space_complexity": "O(1)",
    "description": "Find the number of successful pairs of spells and potions where the product of spell strength and potion strength is at least the success threshold.",
}

def solve(spells: list[int], potions: list[int], success: int) -> list[int]:
    """
    Calculates the number of successful pairs for each spell.

    A pair is successful if spell[i] * potion[j] >= success.

    Args:
        spells: A list of integers representing spell strengths.
        potions: A list of integers representing potion strengths.
        success: The minimum product required for a pair to be successful.

    Returns:
        A list of integers where each element is the count of successful 
        potion pairs for the corresponding spell.

    Examples:
        >>> solve([5, 1, 3], [1, 2, 3, 4, 5], 7)
        [3, 0, 2]
        >>> solve([1], [1], 1)
        [1]
    """
    # Sort potions to enable binary search for the threshold
    potions.sort()
    m = len(potions)
    results = []

    for spell in spells:
        # We need potion >= success / spell. 
        # Using ceiling division logic: (success + spell - 1) // spell
        # to avoid floating point precision issues.
        target_potion = (success + spell - 1) // spell
        
        # Binary search to find the first index where potions[index] >= target_potion
        left = 0
        right = m - 1
        first_valid_index = m
        
        while left <= right:
            mid = (left + right) // 2
            if potions[mid] >= target_potion:
                # This potion works, but there might be a smaller one to the left
                first_valid_index = mid
                right = mid - 1
            else:
                # This potion is too weak, look to the right
                left = mid + 1
        
        # All potions from first_valid_index to the end of the array are successful
        results.append(m - first_valid_index)

    return results
