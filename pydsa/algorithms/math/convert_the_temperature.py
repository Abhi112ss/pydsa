METADATA = {
    "id": 2469,
    "name": "Convert the Temperature",
    "slug": "convert_the_temperature",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Convert a Celsius temperature to Kelvin and return both values.",
}


def solve(temperature: float) -> list[float]:
    """Convert a Celsius temperature to Kelvin.

    Args:
        temperature: Temperature in Celsius.

    Returns:
        A list where the first element is the original Celsius temperature and the
        second element is the equivalent temperature in Kelvin.

    Examples:
        >>> solve(0.0)
        [0.0, 273.15]
        >>> solve(25.0)
        [25.0, 298.15]
    """
    # Apply the conversion formula: Kelvin = Celsius + 273.15
    kelvin_temperature = temperature + 273.15
    return [temperature, kelvin_temperature]