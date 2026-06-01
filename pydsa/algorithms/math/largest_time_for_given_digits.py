METADATA = {
    "id": 949,
    "name": "Largest Time for Given Digits",
    "slug": "largest-time-for-given-digits",
    "category": "Math",
    "aliases": [],
    "tags": ["permutation", "brute_force", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the largest time in HH:MM format that can be formed using four given digits.",
}

import itertools

def solve(digits: list[int]) -> str:
    """
    Finds the largest possible time in HH:MM format using the four provided digits.

    Args:
        digits: A list of four integers representing the available digits.

    Returns:
        A string representing the largest valid time in "HH:MM" format, 
        or "00:00" if no valid time can be formed.

    Examples:
        >>> solve([1, 2, 3, 4])
        '23:41'
        >>> solve([5, 5, 5, 5])
        '00:00'
        >>> solve([0, 0, 0, 0])
        '00:00'
    """
    max_minutes = -1

    # Generate all unique permutations of the 4 digits
    # Since there are only 4! = 24 permutations, this is O(1)
    for permutation in itertools.permutations(digits):
        # Extract digits for hours and minutes
        h1, h2, m1, m2 = permutation
        
        hours = h1 * 10 + h2
        minutes = m1 * 10 + m2

        # Validate the time:
        # 1. Hours must be in range [0, 23]
        # 2. Minutes must be in range [0, 59]
        if hours < 24 and minutes < 60:
            # Convert time to total minutes from 00:00 to easily compare magnitudes
            total_minutes = hours * 60 + minutes
            if total_minutes > max_minutes:
                max_minutes = total_minutes

    # If no valid time was found, return "00:00"
    if max_minutes == -1:
        return "00:00"

    # Convert the maximum minutes back into HH:MM format
    final_hours = max_minutes // 60
    final_minutes = max_minutes % 60
    
    return f"{final_hours:02d}:{final_minutes:02d}"
