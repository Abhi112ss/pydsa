METADATA = {
    "id": 3899,
    "name": "Angles of a Triangle",
    "slug": "angles_of_a_triangle",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the three interior angles of a triangle given its three side lengths using the Law of Cosines.",
}

import math

def solve(a: float, b: float, c: float) -> list[float]:
    """
    Calculates the three interior angles of a triangle given its side lengths.

    The calculation uses the Law of Cosines: c^2 = a^2 + b^2 - 2ab * cos(C),
    which rearranges to: C = arccos((a^2 + b^2 - c^2) / (2ab)).

    Args:
        a: Length of the first side.
        b: Length of the second side.
        c: Length of the third side.

    Returns:
        A list of three floats representing the angles in degrees, 
        sorted in ascending order.

    Examples:
        >>> solve(3.0, 4.0, 5.0)
        [36.86989764584402, 53.13010235415598, 90.0]
        >>> solve(1.0, 1.0, 1.0)
        [60.0, 60.0, 60.0]
    """
    # Law of Cosines: cos(A) = (b^2 + c^2 - a^2) / (2bc)
    # We use math.acos to get the angle in radians, then convert to degrees.
    
    def get_angle(side1: float, side2: float, opposite_side: float) -> float:
        # Calculate the cosine value using the Law of Cosines formula
        cos_val = (side1**2 + side2**2 - opposite_side**2) / (2 * side1 * side2)
        
        # Clamp cos_val to [-1, 1] to handle potential floating point precision errors
        cos_val = max(-1.0, min(1.0, cos_val))
        
        # Convert radians to degrees
        return math.degrees(math.acos(cos_val))

    # Calculate each of the three angles
    angle_a = get_angle(b, c, a)
    angle_b = get_angle(a, c, b)
    angle_c = get_angle(a, b, c)

    # Return the angles sorted in ascending order as per typical requirements
    angles = [angle_a, angle_b, angle_c]
    angles.sort()
    
    return angles
