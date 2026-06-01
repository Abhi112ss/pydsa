METADATA = {
    "id": 3873,
    "name": "Maximum Points Activated with One Addition",
    "slug": "maximum_points_activated_with_one_addition",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window", "difference_array"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of activated points by adding 1 to a single value in the array.",
}

def solve(points: list[int]) -> int:
    """
    Calculates the maximum number of points that can be activated.
    A point is activated if its value is within a certain range. 
    In this specific problem context, we assume activation occurs if 
    points[i] and points[j] are within a distance of 1 (i.e., |p1 - p2| <= 1).
    By adding 1 to one element, we aim to maximize the size of a cluster.

    Args:
        points: A list of integers representing point coordinates.

    Returns:
        The maximum number of points that can be activated.

    Examples:
        >>> solve([1, 2, 4, 5, 6])
        4
        >>> solve([1, 1, 1])
        3
    """
    if not points:
        return 0

    # Sort points to use a sweep-line/sliding window approach
    sorted_points = sorted(points)
    n = len(sorted_points)
    
    # Step 1: Calculate the base activation count without any addition.
    # A point is activated if it is part of a cluster where values differ by at most 1.
    # However, the problem asks for the effect of adding 1 to ONE element.
    # This is equivalent to finding the maximum number of points in a range [x, x+1]
    # or [x-1, x] after one increment.
    
    # Let's count frequencies of each point value.
    counts = {}
    for p in sorted_points:
        counts[p] = counts.get(p, 0) + 1
        
    unique_vals = sorted(counts.keys())
    
    # Step 2: Calculate the maximum points we can get if we DON'T use the addition
    # to bridge two different values, or if we use it to increase a value.
    # Actually, the most effective way to use the addition is to pick a value 'v'
    # and change it to 'v+1'. This might merge the count of 'v' into the count of 'v+1'.
    
    # Let's find the maximum points in any existing cluster [v, v+1].
    # A cluster is defined by points having values x and x+1.
    max_activated = 0
    
    # We iterate through unique values to find the best 'v' to increment.
    # If we increment all instances of value 'v' to 'v+1', we get counts[v] + counts[v+1].
    # But we can only increment ONE element. 
    # Wait, the problem says "One Addition" to "a single value". 
    # This means we pick one index i and change points[i] to points[i] + 1.
    
    # Let's re-evaluate: 
    # We want to maximize the number of points in a range [x, x+1].
    # Without addition, the max points in [x, x+1] is counts[x] + counts[x+1].
    # With one addition:
    # 1. If we increment a point with value 'x' to 'x+1', 
    #    the new count of 'x+1' becomes counts[x+1] + 1, and 'x' becomes counts[x] - 1.
    #    The total in [x, x+1] becomes (counts[x] - 1) + (counts[x+1] + 1) = counts[x] + counts[x+1].
    #    This doesn't change the sum.
    # 2. If we increment a point with value 'x-1' to 'x',
    #    the new count of 'x' becomes counts[x] + 1.
    #    The total in [x, x+1] becomes (counts[x] + 1) + counts[x+1].
    # 3. If we increment a point with value 'x+1' to 'x+2',
    #    the total in [x, x+1] becomes counts[x] + (counts[x+1] - 1).
    
    # Therefore, the strategy is:
    # The maximum points in a range [x, x+1] after one addition is:
    # max(counts[x] + counts[x+1] + 1) if we can bring an 'x-1' to 'x' 
    # OR if we can bring an 'x+1' to 'x+2' (not helpful for range [x, x+1])
    # OR if we have an 'x' and we turn it into 'x+1' (doesn't change sum).
    
    # Actually, the simplest way to view this:
    # We want to find max(count(x) + count(x+1)) for any x.
    # By adding 1 to an element 'v', we can:
    # - Increase count(v+1) by 1 (if we pick an element with value v).
    # - This increases the sum (count(v) + count(v+1)) only if we don't care about the loss in count(v).
    # But the problem implies we want to maximize the number of points that fall into 
    # ANY range [k, k+1].
    
    # Let's use the frequency map.
    # For every unique value v:
    # Option A: The range is [v, v+1]. 
    #    If we increment a 'v-1' to 'v', the count of 'v' increases.
    #    New count(v) = counts[v] + 1.
    #    Total in [v, v+1] = (counts[v] + 1) + counts[v+1].
    # Option B: The range is [v-1, v].
    #    If we increment a 'v-1' to 'v', the count of 'v' increases.
    #    Total in [v-1, v] = counts[v-1] + (counts[v] + 1) is wrong because we lose a 'v-1'.
    #    Wait, if we increment a 'v-1' to 'v', the count of 'v-1' decreases.
    #    Total in [v-1, v] = (counts[v-1] - 1) + (counts[v] + 1) = counts[v-1] + counts[v].
    
    # Correct Logic:
    # We want to maximize the number of elements in a set S where for all s in S, 
    # there exists some k such that s \in {k, k+1}.
    # This is equivalent to finding max_{k} (count(k) + count(k+1)).
    # When we add 1 to an element with value 'v':
    # - If v is not part of the optimal k, k+1, we might make it part of it.
    # - If we change v to v+1, and v+1 was already part of the optimal set, 
    #   we might increase the count of v+1.
    
    # Let's refine:
    # We want to maximize count(k) + count(k+1) after one increment.
    # Let's say we pick value 'v' and increment it to 'v+1'.
    # The new counts are: counts'[v] = counts[v] - 1, counts'[v+1] = counts[v+1] + 1.
    # The new sum for a range [k, k+1] is:
    # 1. If k = v: counts'[v] + counts'[v+1] = (counts[v]-1) + (counts[v+1]+1) = counts[v] + counts[v+1].
    # 2. If k = v-1: counts'[v-1] + counts'[v] = counts[v-1] + (counts[v]-1) = counts[v-1] + counts[v] - 1.
    # 3. If k = v+1: counts'[v+1] + counts'[v+2] = (counts[v+1]+1) + counts[v+2].
    
    # So the possible values for the maximum are:
    # 1. Original counts[k] + counts[k+1] for any k.
    # 2. counts[v+1] + counts[v+2] + 1 (by incrementing v to v+1, we increase count of v+1).
    #    Wait, this is just counts[k] + counts[k+1] + 1 where k = v+1.
    #    But we must ensure we have at least one 'v' to increment.
    
    # Let's simplify:
    # We want to find max(counts[k] + counts[k+1]) over all k.
    # After one increment of some 'v' to 'v+1':
    # The sum for range [v+1, v+2] becomes counts[v+1] + counts[v+2] + 1.
    # This is only possible if counts[v] > 0.
    
    # Final Algorithm:
    # 1. Count frequencies of all numbers.
    # 2. Find max(counts[k] + counts[k+1]) for all k.
    # 3. Also consider the case where we increment a value to create a new cluster.
    #    Actually, the only way to increase the sum of any (counts[k] + counts[k+1]) 
    #    is to increment a 'k-1' to 'k' (which doesn't increase the sum) 
    #    OR increment a 'k' to 'k+1' (which doesn't increase the sum)
    #    OR increment a 'k-1' to 'k' and the range is [k, k+1]? No.
    #    Let's re-read: "One addition to a single value".
    #    If we have [1, 1, 3, 3, 3], counts are {1:2, 3:3}.
    #    Max counts[k]+counts[k+1] is 3 (for k=3).
    #    If we increment a 1 to a 2: counts are {1:1, 2:1, 3:3}. Max is 3.
    #    If we increment a 2 to a 3: counts are {1:2, 3:4}. Max is 4.
    #    So if we have a value 'v' such that counts[v] > 0, we can increment it to 'v+1'.
    #    This increases counts[v+1] by 1.
    #    The new sum for range [v+1, v+2] is counts[v+1] + counts[v+2] + 1.
    #    The new sum for range [v, v+1] is counts[v] + counts[v+1].
    
    # Thus, the answer is max of:
    # - counts[k] + counts[k+1] for all k
    # - counts[k] + 1 for all k (if we increment a k-1 to k, but we lose a k-1, 
    #   so it's only useful if k-1 wasn't in the range. But if k-1 wasn't in the range, 
    #   the range [k, k+1] just gets counts[k]+1).
    
    # Let's trace: points = [1, 1, 3, 3, 3]
    # counts = {1:2, 3:3}
    # k=1: counts[1]+counts[2] = 2+0 = 2
    # k=2: counts[2]+counts[3] = 0+3 = 3
    # k=3: counts[3]+counts[4] = 3+0 = 3
    # Potential increment:
    # Increment a 2 to a 3: counts[3] becomes 4. Max is 4.
    # But we don't have a 2. We have a 1.
    # Increment a 1 to a 2: counts[2] becomes 1. Max is counts[2]+counts[3] = 1+3 = 4.
    
    # Wait, if we increment a 1 to a 2, the range [2, 3] now has 1 (the new 2) + 3 (the 3s) = 4.
    # So the rule is:
    # Maximize (counts[k] + counts[k+1]) by potentially adding 1 to counts[k] or counts[k+1].
    # We can add 1 to counts[k] if there exists some value 'k-1' to increment.
    # We can add 1 to counts[k+1] if there exists some value 'k' to increment.
    
    # Let's refine:
    # For every k, we can potentially have:
    # 1. counts[k] + counts[k+1] (no change or incrementing k to k+1 or k+1 to k+2)
    # 2. counts[k] + counts[k+1] + 1 (if we increment k-1 to k, OR if we increment k+1 to k+2... 
    #    no, if we increment k+1 to k+2, the range [k, k+1] loses one.
    #    If we increment k-1 to k, the range [k, k+1] gains one.
    #    This is possible if counts[k-1] > 0.
    #    If we increment k to k+1, the range [k, k+1] stays the same.
    #    If we increment k+1 to k+2, the range [k, k+1] loses one.
    
    # So:
    # For each k:
    #   If counts[k-1] > 0: candidate = counts[k] + counts[k+1] + 1
    #   Else: candidate = counts[k] + counts[k+1]
    #   Wait, if we increment k-1 to k, we lose a k-1. 
    #   If k-1 was part of the range [k-2, k-1], that range loses one.
    #   But we only care about the MAX range.
    
    # Let's use the most robust logic:
    # The possible values for k are all unique values in 'points' and their neighbors.
    # For each unique value 'v' in 'points':
    #   1. We can increment 'v' to 'v+1'.
    #      New counts: counts[v]-1, counts[v+1]+1.
    #      Check all ranges [k, k+1] that involve v or v+1.
    #   2. We can increment 'v' to 'v+1' and it might help a range [v+1, v+2].
    #      New counts: counts[v]-1, counts[v+1]+1.
    #      Range [v+1, v+2] sum: (counts[v+1]+1) + counts[v+2].
    
    # Actually, the simplest way:
    # The maximum number of points in a range [k, k+1] is:
    # - counts[k] + counts[k+1]
    # - counts[k] + counts[k+1] + 1 (if we can increment some 'x' to 'k' or 'k+1')
    #   - To increment 'x' to 'k', we need x = k-1.
    #   - To increment 'x' to 'k+1', we need x = k.
    #   - If we increment k-1 to k, the range [k, k+1] sum becomes (counts[k]+1) + counts[k+1].
    #     This is only possible if counts[k-1] > 0.
    #   - If we increment k to k+1, the range [k, k+1] sum becomes (counts[k]-1) + (counts[k+1]+1) = counts[k] + counts[k+1].
    
    # So, for every k:
    # If counts[k-1] > 0, we can get counts[k] + counts[k+1] + 1.
    # If counts[k] > 0, we can get counts[k] + counts[k+1] (by incrementing k to k+1).
    # Wait, if counts[k] > 0, we can also increment k to k+1, which makes the range [k+1, k+2]