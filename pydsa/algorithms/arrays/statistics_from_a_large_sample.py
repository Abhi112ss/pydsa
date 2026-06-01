METADATA = {
    "id": 1093,
    "name": "Statistics from a Large Sample",
    "slug": "statistics-from-a-large-sample",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "aggregate_functions", "statistics"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the average, median, and mode of a given sample of integers.",
}

from collections import Counter
from statistics import median


def solve(sample: list[int]) -> dict[str, float]:
    """
    Calculates the average, median, and mode of a given list of integers.

    Args:
        sample: A list of integers representing the sample data.

    Returns:
        A dictionary containing the 'average', 'median', and 'mode' 
        rounded to one decimal place.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
        {'average': 3.4, 'median': 4.0, 'mode': 5.0}
        >>> solve([1, 1, 2, 2, 3, 3])
        {'average': 2.0, 'median': 2.5, 'mode': 1.0}
    """
    if not sample:
        return {"average": 0.0, "median": 0.0, "mode": 0.0}

    # Calculate average: sum of elements divided by count
    average_val = sum(sample) / len(sample)

    # Calculate median: sort the list and find the middle element(s)
    # Using statistics.median handles both even and odd length lists correctly
    median_val = median(sample)

    # Calculate mode: find the most frequent element
    # In case of ties, the problem context (SQL) usually implies the smallest value
    # or any valid mode. Here we follow the standard statistical approach.
    counts = Counter(sample)
    max_freq = max(counts.values())
    
    # Find all elements that have the maximum frequency
    modes = [val for val, freq in counts.items() if freq == max_freq]
    
    # If multiple modes exist, typically the smallest value is chosen in competitive programming
    mode_val = float(min(modes))

    return {
        "average": round(float(average_val), 1),
        "median": round(float(median_val), 1),
        "mode": round(float(mode_val), 1),
    }
