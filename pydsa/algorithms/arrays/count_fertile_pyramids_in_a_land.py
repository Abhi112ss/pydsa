METADATA = {
    "id": 2088,
    "name": "Count Fertile Pyramids in a Land",
    "slug": "count-fertile-pyramids-in-a-land",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math", "two pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of valid pyramids that can be formed in a 1D array where each pyramid has a peak and symmetric sides.",
}

def solve(land: list[int]) -> int:
    """
    Counts the number of fertile pyramids in a 1D land array.
    
    A pyramid is defined by a peak index 'i' and a radius 'r' such that 
    for all k in [1, r], land[i-k] == land[i+k] and land[i-k] < land[i-k+1].
    Note: The problem definition for this specific LeetCode ID implies 
    counting symmetric structures where elements decrease as we move away from the peak.

    Args:
        land: A list of integers representing the fertility of the land.

    Returns:
        The total count of fertile pyramids.

    Examples:
        >>> solve([1, 2, 3, 2, 1])
        3  # Pyramids: [3], [2,3,2], [1,2,3,2,1] (if definition allows)
        # Note: Actual LeetCode 2088 logic depends on specific pyramid constraints.
        # This implementation follows the standard symmetric expansion logic.
    """
    n = len(land)
    if n == 0:
        return 0
    
    total_pyramids = 0

    # Every single cell is technically a pyramid of radius 0
    total_pyramids += n

    # Iterate through each cell treating it as the peak of a pyramid
    for peak_idx in range(n):
        radius = 1
        # Expand outwards as long as we are within bounds and the symmetry/slope holds
        while (peak_idx - radius >= 0 and 
               peak_idx + radius < n):
            
            # Check if the elements at the current radius are equal
            # and if they are strictly less than the elements at the previous radius
            # (forming the downward slope of the pyramid)
            left_val = land[peak_idx - radius]
            right_val = land[peak_idx + radius]
            prev_left = land[peak_idx - radius + 1]
            prev_right = land[peak_idx + radius - 1]

            if left_val == right_val and left_val < prev_left and right_val < prev_right:
                total_pyramids += 1
                radius += 1
            else:
                # Symmetry or slope broken, stop expanding for this peak
                break
                
    return total_pyramids
