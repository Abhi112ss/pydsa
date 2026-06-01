METADATA = {
    "id": 2211,
    "name": "Count Collisions on a Road",
    "slug": "count-collisions-on-a-road",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "simulation", "two-pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the total number of collisions that occur on a road given the initial directions of cars.",
}

def solve(cars: list[int]) -> int:
    """
    Calculates the total number of collisions on a road.

    A collision occurs when a car moving right (1) meets a car moving left (-1).
    When cars collide, they become stationary (0). Stationary cars can then
    be hit by other moving cars, causing further collisions.

    Args:
        cars: A list of integers where 1 represents right, -1 represents left,
              and 0 represents stationary.

    Returns:
        The total number of collisions.

    Examples:
        >>> solve([8, 0, 0, 0])
        0
        >>> solve([1, 0, 0, 0])
        3
        >>> solve([-2, -1, 1, 1, -1, -2])
        6
    """
    n = len(cars)
    left_index = 0
    right_index = n - 1

    # Find the first car that is not stationary (0) from the left
    # Cars at the very left that are already 0 or moving left (-1) 
    # will never collide with anything to their left.
    while left_index < n and cars[left_index] <= 0:
        left_index += 1

    # Find the first car that is not stationary (0) from the right
    # Cars at the very right that are already 0 or moving right (1)
    # will never collide with anything to their right.
    while right_index >= 0 and cars[right_index] >= 0:
        right_index -= 1

    # If no moving cars are found or they don't face each other, collisions = 0
    if left_index >= right_index:
        return 0

    # Any car between the first non-left-moving car and the first non-right-moving car
    # will eventually participate in a collision.
    # For example, in [1, 0, 1, -1], the cars at indices 0, 1, 2, 3 will all collide.
    # The number of collisions is simply the count of elements in this range.
    return right_index - left_index + 1
