METADATA = {
    "id": 195,
    "name": "Tenth Line",
    "slug": "tenth-line",
    "category": "Shell",
    "aliases": [],
    "tags": ["shell"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Print the tenth line of the input stream.",
}

def solve(input_stream: list[str]) -> None:
    """
    Args:
        input_stream: A list of strings representing the lines of input.

    Returns:
        None
    """
    target_index = 9
    if len(input_stream) > target_index:
        print(input_stream[target_index])