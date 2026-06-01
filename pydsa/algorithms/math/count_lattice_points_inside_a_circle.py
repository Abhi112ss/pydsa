METADATA = {
    "id": 2249,
    "name": "Count Lattice Points Inside a Circle",
    "slug": "count-lattice-points-inside-a-circle",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(r^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of integer lattice points that lie inside or on the boundary of a circle defined by its center and radius.",
}

def solve(radius: int, center: list[int]) -> int:
    """
    Counts the number of lattice points (x, y) such that (x - h)^2 + (y - k)^2 <= r^2.

    Args:
        radius: The radius of the circle.
        center: A list of two integers [h, k] representing the center of the circle.

    Returns:
        The total number of integer lattice points inside or on the boundary of the circle.

    Examples:
        >>> solve(2, [0, 0])
        13
        >>> solve(1, [1, 1])
        5
    """
    h, k = center[0], center[1]
    count = 0
    radius_squared = radius * radius

    # The bounding box of the circle is [h - radius, h + radius] x [k - radius, k + radius]
    # We iterate through every integer coordinate within this bounding box.
    for x in range(h - radius, h + radius + 1):
        # Pre-calculate the horizontal distance component to optimize the inner loop
        dx_squared = (x - h) ** 2
        
        for y in range(k - radius, k + radius + 1):
            dy_squared = (y - k) ** 2
            
            # Check if the point (x, y) satisfies the circle equation
            if dx_squared + dy_squared <= radius_squared:
                count += 1
                
    return count
