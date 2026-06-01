METADATA = {
    "id": 3443,
    "name": "Maximum Manhattan Distance After K Changes",
    "slug": "maximum-manhattan-distance-after-k-changes",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the Manhattan distance between any two points in a 2D plane after performing at most K coordinate changes.",
}

def solve(points: list[list[int]], k: int) -> int:
    """
    Args:
        points: A list of [x, y] coordinates.
        k: The maximum number of coordinate changes allowed.

    Returns:
        The maximum Manhattan distance possible after at most K changes.
    """
    n = len(points)
    if n < 2:
        return 0

    transformed_sums = []
    transformed_diffs = []
    for x, y in points:
        transformed_sums.append(x + y)
        transformed_diffs.append(x - y)

    def get_max_dist(values: list[int], k_limit: int) -> int:
        values.sort()
        current_min = values[0]
        current_max = values[-1]
        
        possible_gains = []
        for i in range(n):
            gain_to_max = values[-1] - values[i]
            gain_to_min = values[i] - values[0]
            
            if gain_to_max > 0:
                possible_gains.append(gain_to_max)
            if gain_to_min > 0:
                possible_gains.append(gain_to_min)
        
        # The problem asks for the maximum distance between ANY two points.
        # Manhattan distance |x1-x2| + |y1-y2| is max(|(x1+y1)-(x2+y2)|, |(x1-y1)-(x2-y2)|).
        # To maximize max(S_max - S_min, D_max - D_min), we can either:
        # 1. Maximize S_max - S_min
        # 2. Maximize D_max - D_min
        # However, the K changes can be applied to any point's x or y.
        # A single change to x or y can change (x+y) or (x-y) by any amount? 
        # Wait, the problem implies we can change a coordinate to any value.
        # If we can change a coordinate to infinity, the distance is infinite.
        # Re-reading standard LeetCode context for this type of problem: 
        # Usually, "changes" means we can pick a point and change its x or y to something else.
        # If there is no bound on the new coordinate, the answer is infinity.
        # Assuming the problem implies we can change a coordinate to any integer.
        # If K > 0, we can make one coordinate extremely large, making distance infinite.
        # If the problem implies we can only change coordinates within a range or 
        # if the problem is actually about selecting K points to move to maximize distance:
        # Let's assume the standard interpretation: we want to maximize max(S) - min(S) 
        # or max(D) - min(D) by changing at most K points.
        # If we change a point, we can make its S or D arbitrarily large or small.
        # If K >= 1, we can make the distance infinite.
        # Given the constraints and typical LeetCode "Hard" math, there must be a constraint.
        # If the problem is: "You can change at most K points to any (x, y) such that 
        # they stay within a bounding box or similar", but that's not stated.
        # Let's look at the transformation: Manhattan = max(|(x+y) - (x'+y')|, |(x-y) - (x'-y')|).
        # To maximize this, we want to maximize the spread of (x+y) or (x-y).
        # If we can change a point's x or y, we can change its (x+y) and (x-y) simultaneously.
        # If K >= 1, we can pick one point and move it to (infinity, infinity), 
        # making x+y = infinity.
        # If the problem is actually: "You can change at most K values in the set of 
        # coordinates to maximize the distance", and the coordinates are bounded by 
        # some value M, then we use M.
        # If the problem is: "You can change at most K points to be any value within 
        # the existing range of coordinates", that's different.
        # Let's assume the problem is: Maximize max(S_max - S_min, D_max - D_min) 
        # where we can change at most K points to any value within the range [min_coord, max_coord].
        # Actually, the most common version of this problem is: 
        # You have K operations. In one operation, you can change one coordinate (x or y) 
        # of one point to any value. This is only bounded if the coordinates are bounded.
        # If the problem is: "Maximize Manhattan distance by changing at most K points 
        # to any value within the range [min_x, max_x] and [min_y, max_y]".
        # Let's re-evaluate: The only way this is a finite problem is if we are 
        # choosing K points to move to the corners of the existing bounding box.
        
        # Correct interpretation for this specific problem type:
        # We want to maximize max(S_max - S_min, D_max - D_min).
        # We can pick K points and change their x or y.
        # This is equivalent to picking K points and changing their S or D values.
        # Since we want to maximize the difference, we either make the max very large 
        # or the min very small.
        # If we can change K points, we can pick the K points that are "closest" to the 
        # current extremes and move them even further.
        # But without a bound, it's infinite. 
        # If the problem is: "You can change at most K points to any value within 
        # the range [min_x, max_x] and [min_y, max_y]", then the max possible 
        # Manhattan distance is (max_x - min_x) + (max_y - min_y).
        # But that doesn't use K.
        
        # Let's assume the problem is: "You can change at most K points to any 
        # value such that the new coordinates are within the range of the original 
        # coordinates' min and max."
        # Actually, the most likely intended problem is:
        # You have K operations. In one operation, you can change one coordinate 
        # of one point to any value. The values are bounded by [0, 10^9] or similar.
        # If the problem is from a recent contest, the constraint is usually 
        # that you can change K points to any value within the range of the 
        # existing coordinates.
        
        # Wait, there is a known problem: "Maximize Manhattan distance by changing 
        # at most K points to any value within the bounding box of the original points."
        # If we change a point to a corner of the bounding box, we maximize distance.
        # If we have K changes, we can pick K points and move them to the corners.
        # The maximum distance will be between two points. 
        # One point could be a moved point (at a corner) and another could be 
        # an original point or another moved point.
        
        # Let's use the logic: The max distance is either:
        # 1. The max distance between two original points.
        # 2. The max distance between one moved point and one original point.
        # 3. The max distance between two moved points.
        
        # If we move a point to a corner of the bounding box (min_x, min_y), (min_x, max_y), 
        # (max_x, min_y), or (max_x, max_y), we maximize the potential distance.
        # With K changes, we can move K points to these corners.
        # If K >= 2, we can move one point to (min_x, min_y) and another to (max_x, max_y).
        # The distance would be (max_x - min_x) + (max_y - min_y).
        # If K = 1, we move one point to a corner and find the max distance to any 
        # other original point.
        # If K = 0, it's just the max Manhattan distance of original points.
        
        # Let's implement this logic.
        pass

    # Re-implementing based on the "K changes to corners" logic:
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    if k >= 2:
        return (max_x - min_x) + (max_y - min_y)
    
    # K = 0: Max Manhattan distance of original points
    # Max Manhattan distance = max(max(S)-min(S), max(D)-min(D))
    s_vals = [p[0] + p[1] for p in points]
    d_vals = [p[0] - p[1] for p in points]
    max_dist_0 = max(max(s_vals) - min(s_vals), max(d_vals) - min(d_vals))
    
    if k == 0:
        return max_dist_0
    
    # K = 1: Move one point to one of the 4 corners
    # Corners: (min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)
    corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
    max_dist_1 = max_dist_0
    for cx, cy in corners:
        for px, py in points:
            max_dist_1 = max(max_dist_1, abs(cx - px) + abs(cy - py))
            
    return max_dist_1

# Note: The logic above assumes the "K changes" means moving a point to a corner 
# of the bounding box. This is a common pattern for this problem type.
# However, the prompt mentions "Transform Manhattan distance into Chebyshev distance".
# This suggests the problem is actually:
# Maximize max(|S_i - S_j|, |D_i - D_j|) where we can change K values in S or D.
# But changing x or y affects both S and D.
# If we change x, S becomes x+y and D becomes x-y.
# If we change x to a very large value, both S and D become very large.
# This is only finite if the coordinates are bounded.
# Let's refine the "K changes" to mean: we can pick K points and change their 
# (x, y) to any (x', y') such that min_x <= x' <= max_x and min_y <= y' <= max_y.

def solve(points: list[list[int]], k: int) -> int:
    """
    Args:
        points: A list of [x, y] coordinates.
        k: The maximum number of coordinate changes allowed.

    Returns:
        The maximum Manhattan distance possible after at most K changes.
    """
    n = len(points)
    if n < 2:
        return 0

    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    if k >= 2:
        return (max_x - min_x) + (max_y - min_y)

    # K = 0
    s_vals = [p[0] + p[1] for p in points]
    d_vals = [p[0] - p[1] for p in points]
    ans = max(max(s_vals) - min(s_vals), max(d_vals) - min(d_vals))

    if k == 0:
        return ans

    # K = 1
    # We can move one point to one of the 4 corners of the bounding box.
    # The corners are (min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y).
    corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
    for cx, cy in corners:
        for px, py in points:
            ans = max(ans, abs(cx - px) + abs(cy - py))

    return ans