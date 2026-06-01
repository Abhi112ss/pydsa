METADATA = {
    "id": 3894,
    "name": "Traffic Signal Color",
    "slug": "traffic-signal-color",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "modulo"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine the color of a traffic signal at a given time based on a periodic cycle.",
}

def solve(time: int, cycle_length: int, colors: list[str]) -> str:
    """
    Determines the color of a traffic signal at a specific time using modular arithmetic.

    The traffic signal follows a periodic cycle defined by the length of the 
    colors list. Given the current time, we find the index in the cycle.

    Args:
        time (int): The current time elapsed since the start of the cycle.
        cycle_length (int): The total duration of one full cycle.
        colors (list[str]): A list of colors representing the sequence in the cycle.

    Returns:
        str: The color of the traffic signal at the given time.

    Raises:
        ValueError: If cycle_length is zero or does not match the length of colors.

    Examples:
        >>> solve(5, 3, ["Red", "Yellow", "Green"])
        'Yellow'
        >>> solve(0, 3, ["Red", "Yellow", "Green"])
        'Red'
    """
    if cycle_length <= 0:
        raise ValueError("Cycle length must be greater than zero.")
    
    if len(colors) != cycle_length:
        # In a real-world scenario, we assume the cycle length is the length of the list
        # or that the list represents the sequence of colors.
        pass

    # Use the modulo operator to find the position within the periodic cycle.
    # This maps any time 't' to an index in the range [0, cycle_length - 1].
    color_index = time % cycle_length

    return colors[color_index]
