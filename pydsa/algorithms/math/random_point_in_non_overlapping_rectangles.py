METADATA = {
    "id": 497,
    "name": "Random Point in Non-overlapping Rectangles",
    "slug": "random-point-in-non-overlapping-rectangles",
    "category": "Randomization",
    "aliases": [],
    "tags": ["binary_search", "prefix_sum", "randomization"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Pick a random point from a set of non-overlapping rectangles where each point has an equal probability of being chosen.",
}

import random
import bisect

class Solution:
    def __init__(self, rectangles: list[list[int]]):
        """
        Initializes the Solution object with the given rectangles.

        Args:
            rectangles (list[list[int]]): A list of rectangles where each rectangle 
                is represented as [x1, y1, x2, y2].
        """
        self.rectangles = rectangles
        self.prefix_areas = []
        current_total_area = 0
        
        # Precompute prefix sums of areas to allow O(log n) selection of a rectangle
        for rect in rectangles:
            x1, y1, x2, y2 = rect
            area = (x2 - x1) * (y2 - y1)
            current_total_area += area
            self.prefix_areas.append(current_total_area)
        
        self.total_area = current_total_area

    def pick(self) -> list[int]:
        """
        Picks a random point from the non-overlapping rectangles.

        Returns:
            list[int]: A list [x, y] representing the coordinates of the random point.

        Examples:
            >>> sol = Solution([[1,1,3,3], [5,5,6,6]])
            >>> sol.pick()
            [2, 2] # Example output
        """
        # 1. Pick a random value in the range [1, total_area]
        # We use a random integer to map to the prefix sum buckets
        target = random.randint(1, self.total_area)
        
        # 2. Use binary search to find which rectangle contains this target area
        # bisect_left returns the leftmost insertion point to maintain order
        rect_index = bisect.bisect_left(self.prefix_areas, target)
        
        rect = self.rectangles[rect_index]
        x1, y1, x2, y2 = rect
        
        # 3. Calculate the area offset within the selected rectangle
        # This handles the case where the target falls into a rectangle with area > 1
        prev_area = self.prefix_areas[rect_index - 1] if rect_index > 0 else 0
        area_in_rect = target - prev_area
        
        # 4. Map the area_in_rect back to (x, y) coordinates
        # We treat the rectangle as a flattened 1D array of size (width * height)
        width = x2 - x1
        height = y2 - y1
        
        # To ensure uniform distribution, we treat the area as a 1D index
        # Note: area_in_rect is 1-indexed from the target logic
        # We convert to 0-indexed for coordinate calculation
        idx = area_in_rect - 1
        
        # Calculate row and column in the rectangle's local coordinate system
        # We use height as the 'stride' to map 1D index to 2D (x, y)
        # However, a simpler way is to treat it as:
        # x_offset = idx // height, y_offset = idx % height
        # But to be strictly uniform across all possible integer points, 
        # we must be careful if the problem implies continuous or discrete.
        # LeetCode 497 implies continuous/uniform distribution.
        
        # For continuous uniform distribution:
        # We can pick x and y independently if we treat the area as a product.
        # But since we are picking from a 1D 'target', we map it:
        # Let's use the standard mapping for a 2D grid:
        # x = x1 + (idx // height), y = y1 + (idx % height) is for discrete.
        # For continuous, we can use:
        # x = x1 + (idx / area_of_rect) * width is not quite right.
        
        # Correct approach for continuous uniform distribution:
        # Since we need to pick a point (x, y) such that all points are equally likely:
        # We can pick x uniformly in [x1, x2] and y uniformly in [y1, y2].
        # However, the 'target' method is used to pick the RECTANGLE.
        # Once the rectangle is picked, we pick x and y independently.
        
        # Re-evaluating: The 'target' method is actually used to select the rectangle
        # with probability proportional to its area. Once the rectangle is selected,
        # any point inside it is equally likely.
        
        # Wait, the 'target' method is actually used to pick a rectangle. 
        # Once the rectangle is chosen, we just pick x and y uniformly.
        # Let's refine the pick logic to be more robust.
        
        # Re-implementing pick to be cleaner:
        return self._pick_within_rect(rect)

    def _pick_within_rect(self, rect: list[int]) -> list[int]:
        """
        Helper to pick a uniform point within a specific rectangle.
        """
        x1, y1, x2, y2 = rect
        # random.uniform provides a float for continuous distribution
        return [random.uniform(x1, x2), random.uniform(y1, y2)]

# The above logic in pick() was slightly confused by the 1D mapping.
# The correct way to use prefix sums for this problem is:
# 1. Pick a rectangle based on area weight.
# 2. Pick a point uniformly within that rectangle.

class SolutionCorrected:
    def __init__(self, rectangles: list[list[int]]):
        self.rectangles = rectangles
        self.prefix_areas = []
        total = 0
        for r in rectangles:
            area = (r[2] - r[0]) * (r[3] - r[1])
            total += area
            self.prefix_areas.append(total)
        self.total_area = total

    def pick(self) -> list[float]:
        # Pick a random float in [0, total_area]
        target = random.uniform(0, self.total_area)
        # Find the rectangle
        idx = bisect.bisect_right(self.prefix_areas, target)
        # If target is exactly total_area, bisect_right might return len(rects)
        if idx == len(self.rectangles):
            idx -= 1
            
        r = self.rectangles[idx]
        # Pick x and y uniformly within the chosen rectangle
        return [random.uniform(r[0], r[2]), random.uniform(r[1], r[3])]

# Final implementation following the prompt's requirement for a single solve() style structure
# but adhering to the LeetCode class structure.

class SolutionFinal:
    def __init__(self, rectangles: list[list[int]]):
        self.rects = rectangles
        self.prefix_sums = []
        curr = 0.0
        for r in rectangles:
            area = float((r[2] - r[0]) * (r[3] - r[1]))
            curr += area
            self.prefix_sums.append(curr)
        self.total_area = curr

    def pick(self) -> list[float]:
        """
        Picks a random point from the non-overlapping rectangles.

        Args:
            None (uses self.rects and self.prefix_sums)

        Returns:
            list[float]: A list [x, y] representing the coordinates of the random point.
        """
        # Pick a random value in the range [0, total_area]
        target = random.uniform(0, self.total_area)
        
        # Find the rectangle index using binary search
        # bisect_right finds the first index where prefix_sum > target
        idx = bisect.bisect_right(self.prefix_sums, target)
        
        # Boundary check for floating point precision
        if idx >= len(self.rects):
            idx = len(self.rects) - 1
            
        rect = self.rects[idx]
        
        # Pick x and y independently and uniformly within the selected rectangle
        # This ensures every point in the rectangle has equal probability
        x = random.uniform(rect[0], rect[2])
        y = random.uniform(rect[1], rect[3])
        
        return [x, y]

# To match the LeetCode interface exactly:
class Solution:
    def __init__(self, rectangles: list[list[int]]):
        self.rects = rectangles
        self.prefix_sums = []
        curr = 0.0
        for r in rectangles:
            area = float((r[2] - r[0]) * (r[3] - r[1]))
            curr += area
            self.prefix_sums.append(curr)
        self.total_area = curr

    def pick(self) -> list[float]:
        target = random.uniform(0, self.total_area)
        idx = bisect.bisect_right(self.prefix_sums, target)
        if idx >= len(self.rects):
            idx = len(self.rects) - 1
        rect = self.rects[idx]
        return [random.uniform(rect[0], rect[2]), random.uniform(rect[1], rect[3])]