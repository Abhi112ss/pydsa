METADATA = {
    "id": 3457,
    "name": "Eat Pizzas!",
    "slug": "eat_pizzas",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the total value of pizza slices eaten given a set of slices and a limit on the number of slices that can be eaten.",
}

def solve(pizza_values: list[int], k: int) -> int:
    """
    Calculates the maximum total value of pizza slices that can be eaten.

    The problem asks to pick the top 'k' largest pizza slices to maximize 
    the total value. This is a classic greedy approach.

    Args:
        pizza_values: A list of integers representing the value of each pizza slice.
        k: The maximum number of slices that can be eaten.

    Returns:
        The maximum total value of the slices eaten.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        12
        >>> solve([10, 20, 5, 1], 2)
        30
    """
    # If k is greater than the number of available slices, we eat all slices.
    if k >= len(pizza_values):
        return sum(pizza_values)

    # Sort the pizza values in descending order to pick the largest ones first.
    # This ensures the greedy choice property holds.
    sorted_pizzas = sorted(pizza_values, reverse=True)

    # Sum the first k elements from the sorted list.
    max_value = sum(sorted_pizzas[:k])

    return max_value
