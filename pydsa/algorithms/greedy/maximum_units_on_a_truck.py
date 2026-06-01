METADATA = {
    "id": 1710,
    "name": "Maximum Units on a Truck",
    "slug": "maximum-units-on-a-truck",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum total units that can be carried by a truck with a given capacity by picking boxes with the highest units per box first.",
}

def solve(box_types: list[list[int]], truck_capacity: int) -> int:
    """
    Calculates the maximum total units that can be carried by a truck.

    Args:
        box_types: A list of lists where box_types[i] = [number_of_boxes, units_per_box].
        truck_capacity: The maximum number of boxes the truck can carry.

    Returns:
        The maximum total units that can be carried.

    Examples:
        >>> solve([[1, 3], [2, 2], [3, 1]], 5)
        11
        >>> solve([[5, 10], [4, 5], [2, 2]], 4)
        40
    """
    # Sort the box types by units per box in descending order to apply greedy strategy
    box_types.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    remaining_capacity = truck_capacity

    for num_boxes, units_per_box in box_types:
        if remaining_capacity <= 0:
            break

        # Determine how many boxes of this type we can take
        # We take either all available boxes of this type or whatever fits in the capacity
        take_boxes = min(num_boxes, remaining_capacity)
        
        total_units += take_boxes * units_per_box
        remaining_capacity -= take_boxes

    return total_units
