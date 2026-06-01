METADATA = {
    "id": 1564,
    "name": "Put Boxes Into the Warehouse I",
    "slug": "put-boxes-into-the-warehouse-i",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if all boxes can fit into a warehouse by checking if the sum of box sizes is less than or equal to the capacity.",
}

def solve(boxes: list[int], capacity: int) -> bool:
    """
    Determines if all boxes can be placed into a warehouse given a specific capacity.

    Args:
        boxes: A list of integers representing the size of each box.
        capacity: An integer representing the total capacity of the warehouse.

    Returns:
        True if the sum of all box sizes is less than or equal to the capacity, 
        False otherwise.

    Examples:
        >>> solve([4, 4, 4, 4], 16)
        True
        >>> solve([4, 4, 4, 4], 15)
        False
    """
    # Calculate the total volume required by all boxes
    total_volume_required = sum(boxes)
    
    # Check if the total volume fits within the warehouse capacity
    return total_volume_required <= capacity
