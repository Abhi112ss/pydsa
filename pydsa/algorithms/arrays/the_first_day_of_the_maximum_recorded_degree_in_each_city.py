METADATA = {
    "id": 2314,
    "name": "The First Day of the Maximum Recorded Degree in Each City",
    "slug": "the-first-day-of-the-maximum-recorded-degree-in-each-city",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Find the first day each city recorded its maximum temperature.",
}

def solve(temperature: list[list[int]]) -> list[list[int]]:
    """
    Finds the first day each city recorded its maximum temperature.

    Args:
        temperature: A list of lists where temperature[i] = [city_i, day_i, temp_i].

    Returns:
        A list of lists where each sublist is [city_i, day_i] for the first day 
        the maximum temperature was recorded for that city. The result is 
        sorted by city ID.

    Examples:
        >>> solve([[1,1,10],[1,2,20],[1,3,20],[2,1,30],[2,2,10]])
        [[1, 2], [2, 1]]
        >>> solve([[1,1,10],[1,2,10]])
        [[1, 1]]
    """
    # max_temps stores: {city_id: max_temperature_seen_so_far}
    max_temps: dict[int, int] = {}
    # first_days stores: {city_id: day_of_first_max_temp}
    first_days: dict[int, int] = {}

    for city_id, day, temp in temperature:
        # If city is new or we found a strictly higher temperature
        if city_id not in max_temps or temp > max_temps[city_id]:
            max_temps[city_id] = temp
            first_days[city_id] = day
        # Note: If temp == max_temps[city_id], we do nothing because 
        # we only care about the *first* day it occurred.

    # Extract results and sort by city_id as required by the problem
    sorted_cities = sorted(first_days.keys())
    return [[city, first_days[city]] for city in sorted_cities]
