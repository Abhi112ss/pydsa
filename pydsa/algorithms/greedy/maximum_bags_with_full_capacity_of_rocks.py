METADATA = {
    "id": 2278,
    "name": "Maximum Bags With Full Capacity of Rocks",
    "slug": "maximum-bags-with-full-capacity-of-rocks",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of bags that can be filled to full capacity given a limited number of extra rocks.",
    "extra_info": "Space complexity is O(n) due to the creation of the differences list for sorting."
}

def solve(capacity: list[int], rocks: list[int], extra_rocks: int) -> int:
    """
    Calculates the maximum number of bags that can be filled to their full capacity.

    The strategy is to use a greedy approach: calculate how many more rocks each 
    bag needs to reach its capacity, sort these requirements in ascending order, 
    and fill the bags that need the fewest rocks first.

    Args:
        capacity: A list of integers representing the capacity of each bag.
        rocks: A list of integers representing the current number of rocks in each bag.
        extra_rocks: An integer representing the number of additional rocks available.

    Returns:
        The maximum number of bags that can be fully filled.

    Examples:
        >>> solve([10, 20, 30], [5, 15, 15], 10)
        2
        >>> solve([10, 20, 30], [5, 15, 15], 5)
        1
    """
    # Calculate the deficit for each bag (how many rocks are needed to fill it)
    # We only care about the difference between capacity and current rocks.
    differences = [capacity[i] - rocks[i] for i in range(len(capacity))]

    # Sort the differences to apply a greedy strategy: 
    # Fill the bags that require the least amount of rocks first to maximize count.
    differences.sort()

    full_bags_count = 0
    
    for needed in differences:
        if extra_rocks >= needed:
            # If we have enough rocks to fill this bag, subtract the cost and increment count
            extra_rocks -= needed
            full_bags_count += 1
        else:
            # Since the list is sorted, if we can't fill this bag, we can't fill any subsequent ones
            break

    return full_bags_count
