METADATA = {
    "id": 475,
    "name": "Heaters",
    "slug": "heaters",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sorting", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n log m + m log m)",
    "space_complexity": "O(1)",
    "description": "Find the minimum radius required such that all houses are covered by at least one heater.",
}

def solve(houses: list[int], heaters: list[int]) -> int:
    """
    Calculates the minimum radius required for heaters to cover all houses.

    The algorithm sorts the heaters and, for each house, uses binary search 
    to find the closest heater (either the one immediately to the left 
    or the one immediately to the right). The maximum of these minimum 
    distances is the required radius.

    Args:
        houses: A list of integers representing the positions of houses.
        heaters: A list of integers representing the positions of heaters.

    Returns:
        The minimum radius required to cover all houses.

    Examples:
        >>> solve([1, 2, 3], [2])
        1
        >>> solve([1, 2, 3, 4], [1, 4])
        1
    """
    # Sort heaters to enable binary search
    heaters.sort()
    max_min_distance = 0
    num_heaters = len(heaters)

    for house in houses:
        # Binary search to find the insertion point of the house in the heaters list
        # This tells us which heaters are adjacent to the current house
        low = 0
        high = num_heaters - 1
        idx = num_heaters

        while low <= high:
            mid = (low + high) // 2
            if heaters[mid] >= house:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1

        # idx is the index of the first heater >= house
        # The closest heater is either at idx or idx - 1
        current_min_distance = float('inf')

        # Check heater to the right (if it exists)
        if idx < num_heaters:
            current_min_distance = min(current_min_distance, heaters[idx] - house)
        
        # Check heater to the left (if it exists)
        if idx > 0:
            current_min_distance = min(current_min_distance, house - heaters[idx - 1])

        # The global answer is the maximum of the distances needed for each house
        max_min_distance = max(max_min_distance, int(current_min_distance))

    return max_min_distance
