METADATA = {
    "id": 1007,
    "name": "Minimum Domino Rotations For Equal Row",
    "slug": "minimum-domino-rotations-for-equal-row",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of rotations needed to make all values in either row A or row B equal.",
}

def solve(tops: list[int], bottoms: list[int]) -> int:
    """
    Calculates the minimum number of rotations to make all elements in one row equal.

    The key insight is that if a solution exists, the target value must be 
    present in every domino position, meaning it must be one of the values 
    found in the first domino (tops[0] or bottoms[0]).

    Args:
        tops: A list of integers representing the top row of dominoes.
        bottoms: A list of integers representing the bottom row of dominoes.

    Returns:
        The minimum number of rotations required, or -1 if it is impossible.

    Examples:
        >>> solve([2,1,2,4,2,2], [5,2,6,2,3,2])
        2
        >>> solve([3,8,7], [1,1,1])
        -1
    """
    n = len(tops)

    def check(target: int) -> int:
        """
        Helper to check if it's possible to make a row equal to 'target'.
        Returns the minimum rotations if possible, otherwise infinity.
        """
        rotations_top = 0
        rotations_bottom = 0
        
        for i in range(n):
            # If neither side of the domino has the target, this target is invalid
            if tops[i] != target and bottoms[i] != target:
                return float('inf')
            
            # If top isn't target, we must rotate (bottom must be target)
            elif tops[i] != target:
                rotations_top += 1
            
            # If bottom isn't target, we must rotate (top must be target)
            elif bottoms[i] != target:
                rotations_bottom += 1
                
        # Return the minimum rotations needed to satisfy either row A or row B
        return min(rotations_top, rotations_bottom)

    # The target value MUST be either tops[0] or bottoms[0]
    # If a value exists in every domino, it must exist in the first one.
    result = min(check(tops[0]), check(bottoms[0]))

    return int(result) if result != float('inf') else -1
