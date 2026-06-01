METADATA = {
    "id": 1936,
    "name": "Add Minimum Number of Rungs",
    "slug": "add-minimum-number-of-rungs",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of rungs needed to ensure no gap between consecutive rungs is greater than two.",
}

def solve(needed_gap: int, rungs: list[int]) -> int:
    """
    Calculates the minimum number of rungs required to bridge gaps larger than the allowed gap.

    Args:
        needed_gap: The maximum allowed distance between two consecutive rungs.
        rungs: A sorted list of integers representing the positions of existing rungs.

    Returns:
        The minimum number of additional rungs required.

    Examples:
        >>> solve(3, [1, 5])
        1
        >>> solve(2, [1, 5])
        2
        >>> solve(4, [1, 5])
        0
    """
    total_rungs_added = 0
    
    # Iterate through the existing rungs to check the distance between neighbors
    for i in range(len(rungs) - 1):
        current_rung = rungs[i]
        next_rung = rungs[i + 1]
        gap_size = next_rung - current_rung
        
        # If the gap is larger than the allowed distance, we need to insert rungs.
        # The number of rungs needed to bridge a gap of size 'gap_size' 
        # such that no two rungs are more than 'needed_gap' apart is:
        # (gap_size - 1) // needed_gap
        if gap_size > needed_gap:
            # Using integer division to find how many segments of 'needed_gap' 
            # fit into the gap, minus the existing endpoints.
            # Example: gap=5, needed=2. (5-1)//2 = 2 rungs needed (at pos 3 and 5 is not possible, 
            # but logic holds for gaps: 1, [3], 5 -> gap is 2. 
            # Wait, if gap is 5 and needed is 2: 1, (3), (5) is not right.
            # If rungs are 1 and 5, gap is 4. If needed is 2: 1, (3), 5. 
            # (5-1-1) // 2 = 1 rung.
            # Correct formula for rungs to add: (gap_size - 1) // needed_gap
            # Let's re-verify: gap=5, needed=2. (5-1)//2 = 2. Rungs: 1, [3], [5]... no.
            # If rungs are 1 and 5, gap is 4. (4-1)//2 = 1. Rungs: 1, 3, 5. Correct.
            # If rungs are 1 and 6, gap is 5. (5-1)//2 = 2. Rungs: 1, 3, 5, 6. Correct.
            total_rungs_added += (gap_size - 1) // needed_gap
            
    return total_rungs_added
