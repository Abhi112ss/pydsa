METADATA = {
    "id": 2038,
    "name": "Remove Colored Pieces if Both Neighbors are the Same Color",
    "slug": "remove-colored-pieces-if-both-neighbors-are-the-same-color",
    "category": "Greedy",
    "aliases": [],
    "tags": ["string_matching", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if it is possible to remove all pieces of a specific color given the constraints on neighbor colors.",
}

def solve(colors: str, red_indices: list[int], blue_indices: list[int]) -> bool:
    """
    Determines if all pieces of a specific color can be removed.
    
    A piece can be removed if both its neighbors are of a different color.
    The problem asks if we can remove ALL red pieces OR ALL blue pieces.
    
    Args:
        colors: A string representing the sequence of colors.
        red_indices: A list of indices where the color is 'red'.
        blue_indices: A list of indices where the color is 'blue'.
        
    Returns:
        True if all red pieces can be removed or all blue pieces can be removed, False otherwise.
        
    Examples:
        >>> solve("brbr", [1, 3], [0, 2])
        True
        >>> solve("rrbb", [0, 1], [2, 3])
        False
    """
    
    def can_remove_all(target_indices: list[int]) -> bool:
        """
        Checks if a specific set of indices can be entirely removed.
        
        To remove all pieces of color X, every piece of color X must be 
        adjacent to a piece of color Y (where Y != X). 
        Crucially, for a sequence of color X to be removable, it must not 
        contain any 'trapped' pieces. However, the rule is simpler: 
        If we want to remove all pieces of color X, we must ensure that 
        no two pieces of color X are adjacent in a way that prevents removal.
        Actually, the condition is: we can remove all pieces of color X 
        if and only if no two pieces of color X are adjacent. 
        Wait, the rule is: "a piece can be removed if both its neighbors 
        are of a different color". 
        If we have 'RBR', we can remove 'B'. 
        If we have 'BRB', we can remove 'R'.
        If we want to remove all 'R's, every 'R' must be surrounded by 'B's.
        This means no two 'R's can be adjacent.
        """
        if not target_indices:
            return True
            
        # Check if any two target indices are consecutive
        for i in range(len(target_indices) - 1):
            if target_indices[i+1] == target_indices[i] + 1:
                return False
        return True

    # The problem asks if we can remove ALL red pieces OR ALL blue pieces.
    # To remove all red pieces, no two red pieces can be adjacent.
    # To remove all blue pieces, no two blue pieces can be adjacent.
    return can_remove_all(red_indices) or can_remove_all(blue_indices)
