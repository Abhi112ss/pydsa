METADATA = {
    "id": 478,
    "name": "Generate Random Point in a Circle",
    "slug": "generate-random-point-in-a-circle",
    "category": "Math",
    "aliases": [],
    "tags": ["random", "math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Generate a random point within a circle of radius R such that the distribution is uniform.",
}

import random
import math

class Solution:
    def generate(self, radius: int) -> list[int]:
        """
        Generates a random point (x, y) inside a circle of a given radius.

        To ensure uniform distribution, we cannot simply pick a random radius 
        between 0 and R. If we did, points would cluster near the center. 
        Instead, we use the square root of a uniform random variable for the 
        radius to account for the fact that the area of a circle increases 
        quadratically with the radius.

        Args:
            radius (int): The radius of the circle.

        Returns:
            list[int]: A list containing [x, y] coordinates.

        Examples:
            >>> sol = Solution()
            >>> sol.generate(2)
            [1, -1]  # Example output
        """
        # Generate a random angle in the range [0, 2*pi]
        theta = random.uniform(0, 2 * math.pi)
        
        # Generate a random radius. 
        # We use sqrt(random()) to ensure uniform area distribution.
        # Area of circle is proportional to r^2, so r is proportional to sqrt(U).
        r = radius * math.sqrt(random.random())
        
        # Convert polar coordinates (r, theta) to Cartesian coordinates (x, y)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        
        return [x, y]

def solve():
    """
    Entry point for testing the implementation.
    """
    sol = Solution()
    radius = 5
    # Test multiple samples to verify distribution visually or statistically
    for _ in range(5):
        print(sol.generate(radius))
