METADATA = {
    "id": 1620,
    "name": "Coordinate With Maximum Network Quality",
    "slug": "coordinate-with-maximum-network-quality",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sorting", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find a coordinate that maximizes the sum of signal qualities, where quality decreases with distance.",
}

def solve(quality: list[int], positions: list[list[int]]) -> int:
    """
    Finds the coordinate (x, y) that maximizes the total network quality.
    
    The optimal coordinate must lie on the grid formed by the intersection 
    of the x and y coordinates of the existing signal sources.
    
    Args:
        quality: A list of integers representing the signal quality at each position.
        positions: A list of [x, y] coordinates for each signal source.
        
    Returns:
        An integer representing the coordinate (x * 10^6 + y) that maximizes quality.
        
    Examples:
        >>> solve([10, 8, 5], [[1, 1], [2, 2], [3, 3]])
        1222222
        >>> solve([1, 2, 3], [[1, 1], [2, 2], [3, 3]])
        3333333
    """
    n = len(quality)
    
    # Extract all unique x and y coordinates to form the candidate grid
    # The optimal point must be one of these intersections.
    x_coords = sorted(list(set(p[0] for p in positions)))
    y_coords = sorted(list(set(p[1] for p in positions)))
    
    max_total_quality = -float('inf')
    best_coordinate = 0
    
    # Iterate through every possible intersection in the candidate grid
    for target_x in x_coords:
        for target_y in y_coords:
            current_total_quality = 0
            
            for i in range(n):
                source_x, source_y = positions[i]
                # Manhattan distance calculation
                distance = abs(target_x - source_x) + abs(target_y - source_y)
                
                # If distance is 0, we add the full quality.
                # Otherwise, we add quality - distance, but quality cannot drop below 0.
                current_total_quality += max(0, quality[i] - distance)
            
            # Update the best coordinate found so far.
            # The problem asks for x * 10^6 + y.
            if current_total_quality > max_total_quality:
                max_total_quality = current_total_quality
                best_coordinate = target_x * 10**6 + target_y
            elif current_total_quality == max_total_quality:
                # If qualities are equal, the problem implies we can pick any, 
                # but usually, we follow the order of discovery or specific tie-breaks.
                # The problem statement doesn't specify tie-breaking, but the 
                # grid search naturally handles it.
                pass
                
    return best_coordinate
