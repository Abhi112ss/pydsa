METADATA = {
    "id": 3119,
    "name": "Maximum Number of Potholes That Can Be Fixed",
    "slug": "maximum-number-of-potholes-that-can-be-fixed",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Determine the maximum number of potholes that can be fixed given a limited amount of repair material by prioritizing the smallest repair requirements.",
}

def solve(pothole_requirements: list[int], repair_material: int) -> int:
    """
    Calculates the maximum number of potholes that can be fixed using a greedy approach.

    Args:
        pothole_requirements: A list of integers where each integer represents 
            the amount of material needed to fix a specific pothole.
        repair_material: An integer representing the total amount of material available.

    Returns:
        The maximum number of potholes that can be repaired.

    Examples:
        >>> solve([1, 2, 3], 5)
        2
        >>> solve([10, 20, 30], 5)
        0
        >>> solve([1, 1, 1], 3)
        3
    """
    # Sort the requirements in ascending order to apply the greedy strategy.
    # By fixing the smallest potholes first, we maximize the total count.
    pothole_requirements.sort()

    potholes_fixed = 0
    current_material_used = 0

    for requirement in pothole_requirements:
        # Check if we have enough material left to fix the current smallest pothole.
        if current_material_used + requirement <= repair_material:
            current_material_used += requirement
            potholes_fixed += 1
        else:
            # Since the list is sorted, if we cannot fix this one, 
            # we cannot fix any of the remaining ones.
            break

    return potholes_fixed
