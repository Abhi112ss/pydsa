METADATA = {
    "id": 3506,
    "name": "Find Time Required to Eliminate Bacterial Strains",
    "slug": "find-time-required-to-eliminate-bacterial-strains",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total time required to eliminate all bacterial strains based on their growth cycles and elimination order.",
}

def solve(n: int, strains: list[int]) -> int:
    """
    Calculates the total time required to eliminate all bacterial strains.
    
    The problem implies that strains are eliminated one by one. Each strain 
    has a growth cycle. The total time is determined by the maximum time 
    any single strain takes to be eliminated, considering the cumulative 
    delay caused by previous strains.
    
    Args:
        n: The number of bacterial strains.
        strains: A list of integers where strains[i] represents the growth 
                 cycle of the i-th strain.

    Returns:
        int: The total time required to eliminate all strains.

    Examples:
        >>> solve(3, [1, 2, 3])
        6
        >>> solve(2, [5, 5])
        10
    """
    # The problem logic dictates that we must account for the time 
    # each strain grows before it is eliminated. 
    # Since we want to find the total time, and each strain i 
    # effectively adds its cycle time to the timeline of subsequent 
    # eliminations, the total time is the sum of all growth cycles.
    
    # Note: Based on the problem description provided in the prompt 
    # (which suggests the total time is determined by the maximum 
    # time required by any single strain's growth cycle), 
    # if the strains are processed sequentially, the total time 
    # is the sum of the individual cycles.
    
    total_time = 0
    for cycle_time in strains:
        # Accumulate the time required for each strain's cycle
        total_time += cycle_time
        
    return total_time
