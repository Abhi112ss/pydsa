METADATA = {
    "id": 1482,
    "name": "Minimum Number of Days to Make m Bouquets",
    "slug": "minimum-number-of-days-to-make-m-bouquets",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_val))",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of days required to bloom enough flowers to form m bouquets of k adjacent flowers.",
}

def solve(bloomDay: list[int], m: int, k: int) -> int:
    """
    Finds the minimum number of days required to make m bouquets of k adjacent flowers.

    Args:
        bloomDay: A list of integers where bloomDay[i] is the day the i-th flower blooms.
        m: The number of bouquets required.
        k: The number of adjacent flowers required for each bouquet.

    Returns:
        The minimum number of days required, or -1 if it is impossible.

    Examples:
        >>> solve([1, 10, 3, 10, 2], 3, 1)
        1
        >>> solve([7, 7, 7, 7, 7, 7, 7], 2, 3)
        7
        >>> solve([1, 10, 3, 10, 2], 3, 4)
        -1
    """
    # If the total flowers needed exceeds available flowers, it's impossible.
    if m * k > len(bloomDay):
        return -1

    def can_make_bouquets(days: int) -> bool:
        """Helper to check if m bouquets can be made within the given days."""
        bouquets_count = 0
        adjacent_flowers = 0
        
        for bloom in bloomDay:
            if bloom <= days:
                # Flower has bloomed, increment current adjacent count
                adjacent_flowers += 1
                if adjacent_flowers == k:
                    # We found a complete bouquet
                    bouquets_count += 1
                    adjacent_flowers = 0
            else:
                # Sequence broken, reset adjacent count
                adjacent_flowers = 0
                
            if bouquets_count >= m:
                return True
        return False

    # Binary search range: from the earliest possible bloom to the latest possible bloom
    low = min(bloomDay)
    high = max(bloomDay)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if can_make_bouquets(mid):
            # If possible, try to find a smaller number of days
            result = mid
            high = mid - 1
        else:
            # If not possible, we need more days
            low = mid + 1

    return result
