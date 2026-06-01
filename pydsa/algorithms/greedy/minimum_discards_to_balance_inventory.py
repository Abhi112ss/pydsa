METADATA = {
    "id": 3679,
    "name": "Minimum Discards to Balance Inventory",
    "slug": "minimum-discards-to-balance-inventory",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the minimum number of items to discard so that all remaining items have the same frequency.",
}

def solve(inventory: list[int]) -> int:
    """
    Calculates the minimum number of items to discard so that all remaining 
    item types have the same frequency.

    Args:
        inventory: A list of integers representing the counts of each item type.

    Returns:
        The minimum number of discards required.

    Examples:
        >>> solve([1, 2, 3])
        3
        >>> solve([5, 5, 5])
        0
        >>> solve([1, 1, 2, 2, 3, 3, 3])
        2
    """
    if not inventory:
        return 0

    # Step 1: Count the frequency of each frequency.
    # First, we find how many of each item we have.
    # Then, we count how many item types share the same frequency.
    # Note: The input 'inventory' is already counts of items.
    # If 'inventory' were [item_id, item_id, ...], we would need a Counter first.
    # Based on the problem description, 'inventory' contains the counts.
    
    freq_counts = {}
    total_items = 0
    max_freq = 0
    
    for count in inventory:
        if count > 0:
            freq_counts[count] = freq_counts.get(count, 0) + 1
            total_items += count
            if count > max_freq:
                max_freq = count

    # Step 2: Iterate through all possible target frequencies.
    # A target frequency 'f' means we keep 'f' items for every item type 
    # that currently has at least 'f' items.
    # Any item type with count < f must be discarded entirely.
    # Any item type with count >= f will have (count - f) items discarded.
    
    # To do this efficiently in O(n), we use a prefix sum approach 
    # on the frequency distribution.
    
    # count_of_freq[f] = how many item types have frequency exactly f
    # sum_of_freq[f] = sum of frequencies of all item types with frequency exactly f
    
    count_of_freq = [0] * (max_freq + 1)
    sum_of_freq = [0] * (max_freq + 1)
    
    for count, occurrences in freq_counts.items():
        count_of_freq[count] = occurrences
        sum_of_freq[count] = count * occurrences

    # Convert to suffix sums:
    # suffix_count[f] = number of item types with frequency >= f
    # suffix_sum[f] = sum of frequencies of all item types with frequency >= f
    suffix_count = [0] * (max_freq + 2)
    suffix_sum = [0] * (max_freq + 2)
    
    for i in range(max_freq, 0, -1):
        suffix_count[i] = suffix_count[i + 1] + count_of_freq[i]
        suffix_sum[i] = suffix_sum[i + 1] + sum_of_freq[i]

    min_discards = total_items

    # Step 3: Evaluate each possible target frequency 'f'.
    # If we choose target frequency 'f', the number of items we KEEP is:
    # (number of item types with frequency >= f) * f
    # The number of discards is: total_items - (suffix_count[f] * f)
    
    for f in range(1, max_freq + 1):
        # We only consider f if there's at least one item type that can satisfy it
        if suffix_count[f] > 0:
            kept_items = suffix_count[f] * f
            current_discards = total_items - kept_items
            if current_discards < min_discards:
                min_discards = current_discards

    return min_discards
