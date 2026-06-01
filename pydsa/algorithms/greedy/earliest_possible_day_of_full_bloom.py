METADATA = {
    "id": 2136,
    "name": "Earliest Possible Day of Full Bloom",
    "slug": "earliest-possible-day-of-full-bloom",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the earliest day all flowers are in full bloom by greedily scheduling fertilizer application based on flower bloom duration.",
}

def solve(eventDay: list[int], bloomDay: list[int]) -> int:
    """
    Calculates the earliest day all flowers will be in full bloom.

    The strategy is to sort flowers by their bloom duration in descending order.
    By applying fertilizer to flowers that take longer to bloom first, we 
    minimize the total time required.

    Args:
        eventDay: A list of integers representing the day each flower is planted.
        bloomDay: A list of integers representing the days required for each 
            flower to bloom after being fertilized.

    Returns:
        The earliest day all flowers are in full bloom.

    Examples:
        >>> solve([1, 1, 5], [1, 3, 1])
        6
        >>> solve([1, 10, 3, 10], [10, 1, 1, 1])
        14
    """
    n = len(eventDay)
    # Pair eventDay with bloomDay to keep them linked during sorting
    flowers = []
    for i in range(n):
        flowers.append((eventDay[i], bloomDay[i]))

    # Sort flowers by bloomDay in descending order.
    # Flowers that take longer to bloom should be fertilized as early as possible.
    flowers.sort(key=lambda x: x[1], reverse=True)

    current_day = 0
    max_bloom_day = 0

    for plant_day, duration in flowers:
        # The fertilizer can only be applied on or after the plant_day.
        # If the current_day is earlier than plant_day, we must wait until plant_day.
        current_day = max(current_day, plant_day)
        
        # The flower will bloom at (day fertilizer is applied) + (duration).
        # We track the maximum such day across all flowers.
        max_bloom_day = max(max_bloom_day, current_day + duration)
        
        # Move to the next day for the next fertilizer application.
        current_day += 1

    return max_bloom_day
