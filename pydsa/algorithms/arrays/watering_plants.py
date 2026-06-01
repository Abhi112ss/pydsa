METADATA = {
    "id": 2079,
    "name": "Watering Plants",
    "slug": "watering_plants",
    "category": "simulation",
    "aliases": [],
    "tags": ["simulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Simulate watering plants with a limited water can, counting steps including refills.",
}


def solve(plants: list[int], capacity: int) -> int:
    """Simulate watering the plants in order and count the total steps taken.

    Args:
        plants: A list where plants[i] is the amount of water required for the i‑th plant.
        capacity: The maximum amount of water the can can hold.

    Returns:
        The total number of steps required to water all plants, including steps to move
        between plants and trips back to the river for refilling.

    Examples:
        >>> solve([2, 2, 3, 3], 5)
        14
        >>> solve([1, 2, 3, 4, 5], 5)
        20
    """
    total_steps = 0
    water_left = capacity

    for index, water_needed in enumerate(plants):
        # If the current water is insufficient, go back to the river and refill.
        if water_left < water_needed:
            # Distance back to river and forward to current plant is 2 * index steps.
            total_steps += index * 2
            water_left = capacity

        # Move from previous position (or river) to the current plant.
        total_steps += 1
        water_left -= water_needed

    return total_steps