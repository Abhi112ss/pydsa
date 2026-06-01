METADATA = {
    "id": 3052,
    "name": "Maximize Items",
    "slug": "maximize_items",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the number of items that can be placed into bins given capacity constraints using a greedy approach.",
}

def solve(bins: list[int], items: list[int]) -> int:
    """
    Maximizes the number of items that can be placed into bins.
    
    Each item can be placed in a bin if the bin's capacity is greater than 
    or equal to the item's size. Each bin can hold at most one item.

    Args:
        bins: A list of integers representing the capacity of each bin.
        items: A list of integers representing the size of each item.

    Returns:
        The maximum number of items that can be placed in the bins.

    Examples:
        >>> solve([5, 10, 15], [6, 12, 20])
        2
        >>> solve([1, 2, 3], [1, 2, 3])
        3
        >>> solve([1, 1, 1], [2, 2, 2])
        0
    """
    # Sort both bins and items to allow a greedy two-pointer approach.
    # By sorting, we can match the smallest possible item to the smallest 
    # possible bin that can accommodate it.
    bins.sort()
    items.sort()

    bin_index = 0
    item_index = 0
    count = 0
    
    num_bins = len(bins)
    num_items = len(items)

    # Iterate through both lists using two pointers.
    while bin_index < num_bins and item_index < num_items:
        # If the current bin can fit the current item, place it.
        if bins[bin_index] >= items[item_index]:
            count += 1
            # Move to the next item since this one is placed.
            item_index += 1
            # Move to the next bin since this one is now occupied.
            bin_index += 1
        else:
            # If the bin is too small for the current item, 
            # this bin cannot fit any larger items either.
            # Move to the next larger bin.
            bin_index += 1

    return count
