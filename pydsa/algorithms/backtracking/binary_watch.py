METADATA = {
    "id": 401,
    "name": "Binary Watch",
    "slug": "binary_watch",
    "category": "Algorithms",
    "aliases": [],
    "tags": ["bit_manipulation", "backtracking"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Generate all possible times on a binary watch with a specified number of LEDs illuminated.",
}


def solve(turned_on: int) -> list[str]:
    """Return all possible times on a binary watch with a given number of LEDs on.

    Args:
        turned_on: The total number of LEDs that are illuminated.

    Returns:
        A list of strings representing valid times in "h:mm" format.

    Examples:
        >>> solve(1)
        ['0:01', '0:02', '0:04', '0:08', '0:16', '0:32', '1:00', '2:00', '4:00', '8:00']
        >>> solve(0)
        ['0:00']
    """
    result_times: list[str] = []

    # Helper to count set bits using binary representation.
    def count_set_bits(number: int) -> int:
        return bin(number).count('1')

    # Iterate over all possible hour (0-11) and minute (0-59) values.
    for hour in range(12):
        hour_bits = count_set_bits(hour)
        for minute in range(60):
            minute_bits = count_set_bits(minute)
            # If total illuminated LEDs match the target, format the time.
            if hour_bits + minute_bits == turned_on:
                formatted_time = f"{hour}:{minute:02d}"
                result_times.append(formatted_time)

    return result_times