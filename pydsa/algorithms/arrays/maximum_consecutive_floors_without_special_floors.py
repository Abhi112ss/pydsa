METADATA = {
    "id": 2274,
    "name": "Maximum Consecutive Floors Without Special Floors",
    "slug": "maximum-consecutive-floors-without-special-floors",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of consecutive floors that do not contain any special floors.",
}

def solve(special_floors: list[int], total_floors: int) -> int:
    """
    Calculates the maximum number of consecutive floors without any special floors.

    The problem is solved by sorting the special floors and calculating the 
    gaps between them, including the gaps between the boundaries (1 and total_floors).

    Args:
        special_floors: A list of integers representing the floor numbers that are special.
        total_floors: The total number of floors in the building.

    Returns:
        The maximum number of consecutive non-special floors.

    Examples:
        >>> solve([2, 5], 6)
        2
        >>> solve([1, 5], 6)
        3
        >>> solve([1, 2, 3, 4, 5, 6], 6)
        0
    """
    # Sort the special floors to easily calculate gaps between them
    special_floors.sort()
    
    max_gap = 0
    
    # 1. Check the gap between the first floor (1) and the first special floor
    # If the first special floor is 3, floors 1 and 2 are non-special (gap of 2)
    # Formula: special_floors[0] - 1
    max_gap = max(max_gap, special_floors[0] - 1)
    
    # 2. Check gaps between consecutive special floors
    # If special floors are at 2 and 5, floors 3 and 4 are non-special (gap of 2)
    # Formula: special_floors[i] - special_floors[i-1] - 1
    for i in range(1, len(special_floors)):
        gap = special_floors[i] - special_floors[i - 1] - 1
        if gap > max_gap:
            max_gap = gap
            
    # 3. Check the gap between the last special floor and the top floor (total_floors)
    # If total_floors is 6 and last special floor is 4, floors 5 and 6 are non-special (gap of 2)
    # Formula: total_floors - special_floors[-1]
    max_gap = max(max_gap, total_floors - special_floors[-1])
    
    return max_gap
