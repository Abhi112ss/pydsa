METADATA = {
    "id": 1294,
    "name": "Weather Type in Each Country",
    "slug": "weather_type_in_each_country",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["math", "group_by", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Group temperature data by country and categorize the average temperature into weather types.",
}

def solve(weather_data: list[dict[str, int]]) -> list[dict[str, str]]:
    """
    Groups weather data by country, calculates the average temperature, 
    and categorizes each country into a weather type.

    Args:
        weather_data: A list of dictionaries where each dictionary contains 
            'country' (str) and 'temperature' (int).

    Returns:
        A list of dictionaries containing 'country' and its 'weather_type'.
        Weather types are:
        - 'Hot' if average temperature > 30
        - 'Warm' if 20 <= average temperature <= 30
        - 'Cool' if 10 <= average temperature < 20
        - 'Cold' if average temperature < 10

    Examples:
        >>> data = [{"country": "A", "temperature": 35}, {"country": "A", "temperature": 25}, {"country": "B", "temperature": 5}]
        >>> solve(data)
        [{'country': 'A', 'weather_type': 'Warm'}, {'country': 'B', 'weather_type': 'Cold'}]
    """
    # country_stats maps country name to [sum_of_temperatures, count_of_entries]
    country_stats: dict[str, list[float]] = {}

    # Aggregate temperature sums and counts per country
    for entry in weather_data:
        country = entry["country"]
        temp = entry["temperature"]
        
        if country not in country_stats:
            country_stats[country] = [0.0, 0.0]
        
        country_stats[country][0] += temp
        country_stats[country][1] += 1

    results: list[dict[str, str]] = []

    # Calculate average and determine weather type for each country
    for country, stats in country_stats.items():
        total_temp, count = stats
        avg_temp = total_temp / count

        if avg_temp > 30:
            weather_type = "Hot"
        elif 20 <= avg_temp <= 30:
            weather_type = "Warm"
        elif 10 <= avg_temp < 20:
            weather_type = "Cool"
        else:
            weather_type = "Cold"

        results.append({"country": country, "weather_type": weather_type})

    return results
