METADATA = {
    "id": 2621,
    "name": "Sleep",
    "slug": "sleep",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the total amount of time spent sleeping given a list of wake and sleep times.",
}

def solve(sleep_times: list[int], wake_times: list[int]) -> int:
    """
    Calculates the total duration of sleep based on provided sleep and wake times.

    The problem implies that for each interval i, the person sleeps from 
    sleep_times[i] to wake_times[i]. The total sleep time is the sum of 
    all these durations.

    Args:
        sleep_times: A list of integers representing the start time of each sleep period.
        wake_times: A list of integers representing the end time of each sleep period.

    Returns:
        The total duration of sleep as an integer.

    Examples:
        >>> solve([1, 5], [3, 8])
        5
        >>> solve([10, 20], [15, 25])
        10
    """
    total_sleep_duration = 0
    
    # Iterate through the pairs of sleep and wake times
    # Since the problem guarantees valid intervals, we simply sum the differences
    for sleep_start, wake_end in zip(sleep_times, wake_times):
        total_sleep_duration += (wake_end - sleep_start)
        
    return total_sleep_duration
