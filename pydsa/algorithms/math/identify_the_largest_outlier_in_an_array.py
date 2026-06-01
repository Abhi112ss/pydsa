METADATA = {
    "id": 3371,
    "name": "Identify the Largest Outlier in an Array",
    "slug": "identify-the-largest-outlier-in-an-array",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "statistics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the largest element in an array that is more than two standard deviations away from the mean.",
}

def solve(nums: list[int]) -> int:
    """
    Identifies the largest outlier in an array. An outlier is defined as an 
    element that is more than two standard deviations away from the mean.

    Args:
        nums: A list of integers representing the dataset.

    Returns:
        The largest integer that satisfies the outlier condition. 
        Returns -1 if no such outlier exists.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 100])
        100
        >>> solve([1, 1, 1, 1])
        -1
    """
    n = len(nums)
    if n == 0:
        return -1

    # Step 1: Calculate the arithmetic mean
    total_sum = sum(nums)
    mean = total_sum / n

    # Step 2: Calculate the variance and standard deviation
    # Variance is the average of the squared differences from the mean
    squared_diff_sum = sum((x - mean) ** 2 for x in nums)
    variance = squared_diff_sum / n
    std_dev = variance ** 0.5

    # Step 3: Identify the largest outlier
    # An outlier is defined as |x - mean| > 2 * std_dev
    threshold = 2 * std_dev
    largest_outlier = -1

    for x in nums:
        if abs(x - mean) > threshold:
            if x > largest_outlier:
                largest_outlier = x

    return largest_outlier
