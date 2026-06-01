METADATA = {
    "id": 1322,
    "name": "Ads Performance",
    "slug": "ads-performance",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the click-through rate (CTR) for each ad, represented as a percentage, rounded to the nearest integer.",
}

def solve(clicks: list[int], views: list[int]) -> list[int]:
    """
    Calculates the click-through rate (CTR) for each ad.

    The CTR is defined as (clicks / (clicks + views)) * 100.
    The result is rounded to the nearest integer. If the denominator is 0, 
    the CTR is 0.

    Args:
        clicks: A list of integers representing the number of clicks for each ad.
        views: A list of integers representing the number of views for each ad.

    Returns:
        A list of integers representing the rounded CTR percentage for each ad.

    Examples:
        >>> solve([1, 1], [1, 10])
        [50, 9]
        >>> solve([1, 1], [1, 1])
        [50, 50]
    """
    results: list[int] = []
    
    # Iterate through both lists simultaneously using zip
    for click, view in zip(clicks, views):
        total_interactions = click + view
        
        if total_interactions == 0:
            results.append(0)
            continue
            
        # Calculate CTR as a percentage: (clicks / total) * 100
        # To round to the nearest integer correctly in Python:
        # We use the standard rounding logic. Since we need to round 0.5 up,
        # and Python's round() uses "round half to even", we can use 
        # int(value + 0.5) for positive numbers to ensure standard rounding.
        ctr_percentage = (click * 100) / total_interactions
        
        # Adding 0.5 and taking the floor is a common trick for 
        # rounding positive floats to the nearest integer.
        results.append(int(ctr_percentage + 0.5))
        
    return results
