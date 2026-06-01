METADATA = {
    "id": 605,
    "name": "Can Place Flowers",
    "slug": "can_place_flowers",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if n new flowers can be planted in a flowerbed without violating the no-adjacent rule.",
}


def solve(flowerbed: list[int], n: int) -> bool:
    """Determine if n new flowers can be planted without adjacent flowers.

    Args:
        flowerbed: List of integers where 0 represents an empty plot and 1 a plot with a flower.
        n: Number of new flowers to plant.

    Returns:
        True if it is possible to plant n flowers following the no-adjacent rule, otherwise False.

    Examples:
        >>> solve([1,0,0,0,1], 1)
        True
        >>> solve([1,0,0,0,1], 2)
        False
        >>> solve([0,0,0,0,0], 2)
        True
    """
    # If no flowers need to be planted, the condition is trivially satisfied.
    if n == 0:
        return True

    placed_flowers = 0
    index = 0
    length = len(flowerbed)

    while index < length:
        # Check if the current plot is empty and both neighbors (if they exist) are empty.
        if (
            flowerbed[index] == 0
            and (index == 0 or flowerbed[index - 1] == 0)
            and (index == length - 1 or flowerbed[index + 1] == 0)
        ):
            # Plant a flower here.
            flowerbed[index] = 1
            placed_flowers += 1
            if placed_flowers >= n:
                return True
            # Skip the next plot because we cannot plant adjacent flowers.
            index += 2
        else:
            index += 1

    return placed_flowers >= n