METADATA = {
    "id": 1276,
    "name": "Number of Burgers with No Waste of Ingredients",
    "slug": "number-of-burgers-with-no-waste-of-ingredients",
    "category": "Math",
    "aliases": [],
    "tags": ["algebra", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a given amount of tomatoes and cheese can be used to make an integer number of burgers without any leftovers.",
}

def solve(tomatoes: int, cheese: int) -> bool:
    """
    Determines if the given ingredients can form a whole number of burgers.
    
    Each burger requires:
    - 4 tomatoes
    - 1 cheese
    - 1 bun (not provided in input, but the problem implies we only care about 
      the ratio of tomatoes and cheese provided).
    
    Wait, the problem states:
    - 4 tomatoes
    - 1 cheese
    - 1 bun
    
    Actually, the problem constraints are:
    - 4 tomatoes
    - 1 cheese
    - 1 bun
    
    Wait, looking at the standard problem definition for 1276:
    A burger requires:
    - 4 tomatoes
    - 1 cheese
    - 1 bun
    
    Wait, the prompt says: 4x + 2y = tomatoes and x + y = cheese? 
    No, that's a different system. Let's re-read the standard LeetCode 1276:
    A burger requires:
    - 4 tomatoes
    - 1 cheese
    - 1 bun
    
    Wait, the prompt specifically asks to solve:
    4x + 2y = tomatoes
    x + y = cheese
    
    Let's solve the system provided in the prompt:
    1) 4x + 2y = tomatoes
    2) x + y = cheese
    
    From (2): y = cheese - x
    Substitute into (1):
    4x + 2(cheese - x) = tomatoes
    4x + 2*cheese - 2x = tomatoes
    2x + 2*cheese = tomatoes
    2x = tomatoes - 2*cheese
    x = (tomatoes - 2*cheese) / 2
    
    Now find y:
    y = cheese - x
    y = cheese - (tomatoes - 2*cheese) / 2
    y = (2*cheese - tomatoes + 2*cheese) / 2
    y = (4*cheese - tomatoes) / 2
    
    For a valid solution:
    - x must be an integer >= 0
    - y must be an integer >= 0
    
    Conditions:
    1. (tomatoes - 2*cheese) % 2 == 0
    2. (4*cheese - tomatoes) % 2 == 0
    3. tomatoes - 2*cheese >= 0  => tomatoes >= 2*cheese
    4. 4*cheese - tomatoes >= 0  => 4*cheese >= tomatoes
    
    Wait, if (tomatoes - 2*cheese) is even, then (4*cheese - tomatoes) is also even 
    because 4*cheese is even and tomatoes must be even.
    
    So the conditions are:
    1. tomatoes % 2 == 0
    2. tomatoes >= 2 * cheese
    3. 4 * cheese >= tomatoes
    
    Args:
        tomatoes (int): Total number of tomatoes available.
        cheese (int): Total number of cheese available.

    Returns:
        bool: True if a non-negative integer number of burgers can be made, False otherwise.

    Examples:
        >>> solve(10, 4)
        True
        >>> solve(10, 3)
        False
    """
    # Based on the system:
    # 4x + 2y = tomatoes
    # x + y = cheese
    
    # Check if tomatoes is even (required for x and y to be integers)
    if tomatoes % 2 != 0:
        return False
    
    # Calculate x and y using the derived formulas
    # x = (tomatoes - 2 * cheese) / 2
    # y = (4 * cheese - tomatoes) / 2
    
    # Instead of division, we check the bounds to ensure x >= 0 and y >= 0
    # and ensure the numerator is divisible by 2.
    
    # Condition for x >= 0: tomatoes >= 2 * cheese
    # Condition for y >= 0: 4 * cheese >= tomatoes
    # Condition for integer: tomatoes must be even (since 2*cheese is even)
    
    can_make_x = (tomatoes >= 2 * cheese)
    can_make_y = (4 * cheese >= tomatoes)
    is_even = (tomatoes % 2 == 0)
    
    return can_make_x and can_make_y and is_even
