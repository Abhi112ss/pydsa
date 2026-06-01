METADATA = {
    "id": 2105,
    "name": "Watering Plants II",
    "slug": "watering-plants-ii",
    "category": "Simulation",
    "aliases": [],
    "tags": ["greedy", "simulation"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Simulate a gardener watering plants with limited water capacity and a requirement to return to a river to refill.",
}

def solve(plants: list[int]) -> int:
    """
    Calculates the total steps taken by a gardener to water all plants.

    The gardener starts at position -1, moves to plant 0, and must return to 
    the river (position -1) whenever the current water level is insufficient 
    for the next plant.

    Args:
        plants: A list of integers where plants[i] is the amount of water 
            needed for the i-th plant.

    Returns:
        The total number of steps taken.

    Examples:
        >>> solve([2, 2, 3, 3])
        14
        >>> solve([1, 1, 1, 1])
        10
    """
    total_steps = 0
    current_water = len(plants)
    current_position = -1
    
    for i, water_needed in enumerate(plants):
        # Check if we have enough water for the current plant
        if current_water < water_needed:
            # Step 1: Move from current position back to the river (position -1)
            # Step 2: Move from the river back to the current plant (position i)
            # The distance from current_position to -1 is (current_position - (-1))
            # The distance from -1 to i is (i - (-1))
            steps_to_refill = (current_position - (-1)) + (i - (-1))
            total_steps += steps_to_refill
            
            # Refill water to full capacity
            current_water = len(plants)
            # Update position to the plant we are about to water
            current_position = i
        else:
            # Move from current position to the next plant
            total_steps += (i - current_position)
            current_position = i
            
        # Water the plant
        current_water -= water_needed
        
    return total_steps
