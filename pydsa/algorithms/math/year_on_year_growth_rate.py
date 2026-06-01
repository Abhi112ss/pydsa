METADATA = {
    "id": 3214,
    "name": "Year on Year Growth Rate",
    "slug": "year_on_year_growth_rate",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the year-on-year growth rate for a sequence of values using the formula ((current - previous) / previous) * 100.",
}

def solve(values: list[float]) -> list[float]:
    """
    Calculates the year-on-year growth rate for a given list of values.

    The growth rate is calculated as: ((current - previous) / previous) * 100.
    The resulting list will have a length of len(values) - 1.

    Args:
        values: A list of numerical values representing data over consecutive years.

    Returns:
        A list of floats representing the percentage growth rates between consecutive years.

    Examples:
        >>> solve([100.0, 110.0, 121.0])
        [10.0, 10.0]
        >>> solve([50.0, 40.0, 60.0])
        [-20.0, 50.0]
    """
    if len(values) < 2:
        return []

    growth_rates = []
    
    # Iterate through the list starting from the second element
    for i in range(1, len(values)):
        previous_value = values[i - 1]
        current_value = values[i]
        
        # Avoid division by zero if the previous value is 0
        # In real-world scenarios, growth from 0 is often undefined or handled specially
        if previous_value == 0:
            # If current is also 0, growth is 0; if current > 0, growth is technically infinite
            # For standard algorithmic problems, we assume non-zero denominators or follow specific rules
            growth_rate = 0.0 if current_value == 0 else float('inf')
        else:
            # Apply the standard YoY formula: ((V_new - V_old) / V_old) * 100
            growth_rate = ((current_value - previous_value) / previous_value) * 100.0
            
        growth_rates.append(growth_rate)
        
    return growth_rates
