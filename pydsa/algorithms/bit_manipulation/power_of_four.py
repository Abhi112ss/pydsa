METADATA = {
    "id": 342,
    "name": "Power of Four",
    "slug": "power-of-four",
    "category": "Math",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a given integer is a power of four.",
}

def solve(n: int) -> bool:
    """
    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is a power of four, False otherwise.
    """
    if n <= 0:
        return False
    
    is_power_of_two = (n & (n - 1)) == 0
    
    is_even_bit_position = (n & 0x55555555) != 0
    
    return is_power_of_two and is_even_bit_position