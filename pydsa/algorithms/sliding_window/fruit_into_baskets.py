METADATA = {
    "id": 904,
    "name": "Fruit Into Baskets",
    "slug": "fruit-into-baskets",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest contiguous subarray that contains at most two distinct integers.",
}

def solve(fruits: list[int]) -> int:
    """
    Finds the maximum number of fruits that can be collected using two baskets.
    Each basket can only hold one type of fruit.

    Args:
        fruits: A list of integers where fruits[i] is the type of fruit at tree i.

    Returns:
        The maximum number of fruits that can be collected in a contiguous subarray.

    Examples:
        >>> solve([1, 2, 1])
        3
        >>> solve([0, 1, 2, 2])
        3
        >>> solve([1, 2, 3, 2, 2])
        4
    """
    # Dictionary to keep track of the count of each fruit type in the current window
    fruit_counts: dict[int, int] = {}
    max_fruits: int = 0
    left_pointer: int = 0

    for right_pointer in range(len(fruits)):
        current_fruit = fruits[right_pointer]
        # Add the current fruit to our window
        fruit_counts[current_fruit] = fruit_counts.get(current_fruit, 0) + 1

        # If we have more than 2 types of fruit, shrink the window from the left
        while len(fruit_counts) > 2:
            left_fruit = fruits[left_pointer]
            fruit_counts[left_fruit] -= 1
            
            # If the count drops to zero, remove the fruit type from the dictionary
            if fruit_counts[left_fruit] == 0:
                del fruit_counts[left_fruit]
            
            left_pointer += 1

        # Calculate the current window size and update the maximum
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_fruits:
            max_fruits = current_window_size

    return max_fruits
