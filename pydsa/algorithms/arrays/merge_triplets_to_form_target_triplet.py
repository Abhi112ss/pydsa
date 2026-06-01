METADATA = {
    "id": 1899,
    "name": "Merge Triplets to Form Target Triplet",
    "slug": "merge-triplets-to-form-target-triplet",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a target triplet can be formed by merging given triplets such that no element in the merged triplet exceeds the target.",
}

def solve(triplets: list[list[int]], target: list[int]) -> bool:
    """
    Determines if the target triplet can be formed by merging the given triplets.
    
    A triplet can be used if all its elements are less than or equal to the 
    corresponding elements in the target. We track which indices of the target 
    can be satisfied by such valid triplets.

    Args:
        triplets: A list of triplets where each triplet is a list of 3 integers.
        target: A list of 3 integers representing the target triplet.

    Returns:
        True if the target triplet can be formed, False otherwise.

    Examples:
        >>> solve([[2, 5, 3], [5, 2, 3], [4, 2, 4], [1, 2, 2]], [5, 5, 5])
        True
        >>> solve([[7, 7, 7], [1, 1, 1]], [2, 2, 2])
        False
    """
    # Track which positions in the target (0, 1, or 2) have been satisfied
    satisfied_indices = [False, False, False]
    
    for triplet in triplets:
        # Check if the current triplet is "safe" to use.
        # A triplet is safe if none of its elements exceed the target's elements.
        is_safe = (
            triplet[0] <= target[0] and 
            triplet[1] <= target[1] and 
            triplet[2] <= target[2]
        )
        
        if is_safe:
            # If safe, this triplet can contribute to satisfying the target 
            # at any index where its value matches the target value.
            for i in range(3):
                if triplet[i] == target[i]:
                    satisfied_indices[i] = True
                    
    # If all three positions in the target have been satisfied by at least 
    # one safe triplet, we can form the target.
    return all(satisfied_indices)
