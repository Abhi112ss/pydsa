METADATA = {
    "id": 1739,
    "name": "Building Boxes",
    "slug": "building-boxes",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum cost to build a set of boxes with specific volumes using available building rules.",
}

def solve(volumes: list[int]) -> int:
    """
    Args:
        volumes: A list of integers representing the required volumes of boxes.

    Returns:
        The minimum cost to build all required boxes.
    """
    total_cost = 0
    current_box_count = 0
    current_box_volume = 0
    
    sorted_volumes = sorted(volumes)
    
    for volume in sorted_volumes:
        if volume > current_box_volume:
            total_cost += current_box_count * current_box_volume
            current_box_count = 1
            current_box_volume = volume
        else:
            current_box_count += 1
            
        total_cost += volume
        
    total_cost += current_box_count * current_box_volume
    
    return total_cost