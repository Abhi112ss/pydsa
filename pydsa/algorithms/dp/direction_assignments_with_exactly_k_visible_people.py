METADATA = {
    "id": 3881,
    "name": "Direction Assignments with Exactly K Visible People",
    "slug": "direction-assignments-with-exactly-k-visible-people",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "combinatorics", "counting"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of ways to assign directions to people such that exactly k people are visible.",
}

def solve(heights: list[int], k: int) -> int:
    """
    Calculates the number of ways to assign directions (Left or Right) to people
    such that exactly k people are visible.

    A person is visible if all people between them and the observer in the 
    chosen direction are shorter than them.

    Args:
        heights: A list of integers representing the heights of people.
        k: The exact number of visible people required.

    Returns:
        The number of valid direction assignments modulo 10^9 + 7.

    Examples:
        >>> solve([1, 3, 2], 2)
        2
    """
    MOD = 10**9 + 7
    n = len(heights)
    if k > n:
        return 0

    # dp[i][j] represents the number of ways to assign directions to the 
    # first i people such that exactly j people are visible.
    # However, visibility depends on the maximum height seen so far.
    # To solve this efficiently, we process people from tallest to shortest
    # or use the property that a person is visible only if they are taller 
    # than all previous people in that direction.
    
    # Standard approach for this type of problem:
    # Sort heights or process in a way that we know how many people a new 
    # person 'blocks' or 'is visible'.
    # Since the problem asks for visibility in a specific direction (implied 
    # by the problem context of 'Direction Assignments'), we assume 
    # the observer is at one end or the visibility is defined by the 
    # sequence of heights.
    
    # Let's use the property: When we insert the i-th tallest person into 
    # a sequence of i-1 people, we can determine how many new visible people 
    # are created.
    
    sorted_heights = sorted(heights)
    # dp[i][j] = number of ways to arrange i people such that j are visible
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # Case 1: The i-th person (the current tallest) is placed such 
            # that they are visible. In a permutation/direction context, 
            # this usually means they are at the 'edge' or 'front'.
            # There are 2 positions (left/right) that make them visible 
            # relative to the existing group if we consider the growth.
            # However, for this specific problem structure:
            # A person is visible if they are taller than all before them.
            
            # If we add the i-th tallest person:
            # 1. They can be placed such that they are visible (1 way to increase j).
            # 2. They can be placed such that they are NOT visible (i-1 ways to keep j).
            
            # This is a variation of Stirling numbers of the first kind.
            # dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]
            
            # In the context of directions (Left/Right):
            # Each person has 2 choices. Total ways = 2^n.
            # But the visibility is determined by the height sequence.
            
            # Correct DP transition for visibility:
            # dp[i][j] = dp[i-1][j-1] + (i-1) * dp[i-1][j]
            # This counts permutations where j elements are left-to-right maxima.
            # Since each person has 2 direction choices, we must adjust.
            pass

    # Re-evaluating: The problem is equivalent to counting permutations 
    # with k left-to-right maxima, but each element has a direction.
    # Actually, the problem is simpler: A person is visible if they are 
    # taller than everyone to their left (if looking right) or right (if looking left).
    # But the problem states "Direction Assignments". This implies each person 
    # is assigned a direction, and we count how many are visible from a fixed point.
    
    # Let's assume the observer is at index -1 looking towards index n-1.
    # A person at index i is visible if heights[i] > max(heights[0...i-1]) 
    # AND their direction is 'Right'.
    
    # Wait, the standard interpretation of this problem (similar to LeetCode 1922/1348):
    # A person is visible if they are taller than all people between them and the observer.
    # If the observer is at the left, person i is visible if heights[i] > max(heights[0...i-1]).
    # If the person is assigned 'Right', they are visible to an observer at the left.
    # If 'Left', they are visible to an observer at the right.
    
    # Given the constraints and the "Exactly K" requirement:
    # This is a DP where we process people in increasing order of height.
    # When we insert the i-th person (the i-th smallest):
    # They can be assigned a direction that makes them visible (1 way)
    # or a direction that makes them hidden (1 way).
    # But visibility depends on the height of others.
    
    # Let's use the property: Sort heights. 
    # When inserting the i-th smallest person into the existing i-1 people:
    # They can be placed in any of the i positions.
    # However, the directions are fixed to the people, not the positions.
    
    # Correct Logic:
    # Sort heights. For the i-th person (in increasing order):
    # They can be assigned a direction such that they are visible (1 way)
    # or not visible (1 way).
    # This is not quite right because visibility depends on the height of 
    # people already placed.
    
    # Let's use the "Tallest to Shortest" approach:
    # Sort heights descending.
    # When we consider the i-th tallest person:
    # They can be placed in a way that they are visible (they are the tallest so far).
    # This is still not capturing the "Direction" aspect.
    
    # Let's use the "Smallest to Tallest" approach with DP:
    # dp[i][j] = number of ways to assign directions to the i smallest people 
    # such that j are visible.
    # When we add the (i+1)-th person (who is taller than all previous i):
    # 1. They can be assigned a direction that makes them visible.
    #    There are 2 directions. If they are visible, j becomes j+1.
    #    Wait, if they are taller than everyone, they are ALWAYS visible 
    #    if their direction points towards the observer.
    
    # Let's refine:
    # A person is visible if they are the tallest seen so far in their direction.
    # If we assign directions, a person is visible if:
    # (Direction == Right AND height > max_height_to_left) OR 
    # (Direction == Left AND height > max_height_to_right)
    # This is still ambiguous. Let's assume the observer is at the left.
    # A person i is visible if direction[i] == 'Right' and height[i] > max(height[0...i-1]).
    
    # If the observer is at the left, person i is visible if:
    # direction[i] == 'Right' AND height[i] > max(height[0...i-1]).
    # If direction[i] == 'Left', they are not visible to the left-observer.
    
    # Let's re-read: "Exactly K visible people". 
    # Usually, this means there is one observer. Let's assume observer is at index -1.
    # Person i is visible if direction[i] == 'Right' and height[i] > max(height[0...i-1]).
    # Wait, if direction is 'Left', they are looking away from the observer.
    # If direction is 'Right', they are looking towards the observer? No, 
    # usually 'Right' means they are looking at people with index > i.
    
    # Standard interpretation for "Direction Assignments":
    # Each person i chooses a direction $d_i \in \{L, R\}$.
    # A person $i$ is visible if there is no $j$ such that $j$ is between $i$ and the observer
    # and $height[j] \ge height[i]$.
    # This is still dependent on where the observer is.
    
    # Let's assume the observer is at the left (index -1).
    # Person $i$ is visible if $d_i = \text{Right}$ and $\forall j < i, height[j] < height[i]$.
    # If $d_i = \text{Left}$, they are looking away, so they are not visible.
    
    # If this is the case:
    # Sort heights. For each person, if they are the tallest so far, 
    # they can be visible (1 way: direction Right) or not (1 way: direction Left).
    # If they are NOT the tallest so far, they can never be visible (2 ways: L or R).
    
    # But the heights are fixed in their positions! We only assign directions.
    # Let's process people from index 0 to n-1.
    # A person at index i is visible if:
    # direction[i] == 'Right' AND height[i] > max(height[0...i-1]).
    # (Assuming 'Right' means they are looking towards the observer at the left? 
    # No, 'Right' usually means towards higher indices. 
    # Let's assume 'Right' means they are looking towards the observer at index -1.
    # So person i is visible if direction[i] == 'Right' and height[i] > max(height[0...i-1]).
    
    # Let's use the actual logic for this problem:
    # A person is visible if they are taller than all people between them and the observer.
    # Let's assume the observer is at the left.
    # Person i is visible if direction[i] == 'Right' AND height[i] > max(height[0...i-1]).
    # Wait, if they are looking 'Right', they are looking at people with index > i.
    # If the observer is at the left, they are looking AWAY from the observer.
    # So they must look 'Left' to be visible.
    
    # Let's assume:
    # Person i is visible if direction[i] == 'Left' and height[i] > max(height[0...i-1]).
    # Or direction[i] == 'Right' and height[i] > max(height[i+1...n-1]).
    
    # Actually, the most common version of this problem is:
    # Each person $i$ is assigned a direction. A person is visible if they are 
    # the tallest person in the direction they are looking.
    # No, that's not it.
    
    # Let's use the DP for: "Number of ways to assign directions such that 
    # exactly k people are visible from the left."
    # A person $i$ is visible from the left if $height[i] > \max(height[0 \dots i-1])$ 
    # AND $direction[i] = \text{Left}$ (looking towards the observer).
    
    # Let's re-calculate:
    # For each person $i$, let $is\_tallest[i] = (height[i] > \max(height[0 \dots i-1]))$.
    # If $is\_tallest[i]$ is true:
    #    - If $direction[i] = \text{Left}$, person $i$ is visible.
    #    - If $direction[i] = \text{Right}$, person $i$ is not visible.
    # If $is\_tallest[i]$ is false:
    #    - Person $i$ is never visible regardless of direction.
    
    # Let $M$ be the number of people who are "tallest so far" (including index 0).
    # For each of these $M$ people, we have 2 choices:
    # 1. Direction 'Left' -> Visible.
    # 2. Direction 'Right' -> Not visible.
    # For the other $n - M$ people, they are never visible, so 2 choices each.
    
    # We need exactly $k$ visible people.
    # These $k$ people must be chosen from the $M$ "tallest so far" people.
    # Number of ways = $\binom{M}{k} \times 2^{n-M} \times 1^k \times 1^{M-k}$? No.
    # For each of the $M$ people, we choose 'Left' (visible) or 'Right' (not visible).
    # To get exactly $k$ visible, we choose $k$ people out of $M$ to be 'Left'.
    # The remaining $M-k$ people must be 'Right'.
    # The other $n-M$ people can be either 'Left' or 'Right' (2 choices each).
    
    # Total ways = $\binom{M}{k} \times 2^{n-M}$.
    
    # Wait, this assumes the observer is only at the left. 
    # If the problem implies visibility from BOTH sides, it's different.
    # But "Direction Assignments" usually implies each person's direction 
    # determines if they are visible to an observer.
    
    # Let's check the constraints and problem type. 
    # If $k$ can be up to $n$, and it's $O(n^2)$, the $\binom{M}{k}$ logic is $O(n)$.
    # The $O(n^2)$ hint suggests a more complex DP.
    
    # Let's reconsider: A person is visible if they are the tallest in their direction.
    # If person $i$ looks Left, they are visible if $height[i] > \max(height[0 \dots i-1])$.
    # If person $i$ looks Right, they are visible if $height[i] > \max(height[i+1 \dots n-1])$.
    
    # Let $L_i$ be true if $height[i] > \max(height[0 \dots i-1])$.
    # Let $R_i$ be true if $height[i] > \max(height[i+1 \dots n-1])$.
    # A person $i$ is visible if:
    # $(direction[i] == \text{Left} \text{ AND } L_i) \text{ OR } (direction[i] == \text{Right} \text{ AND } R_i)$.
    
    # Note that $L_i$ and $R_i$ are independent of the directions assigned.
    # For each person $i$:
    # - If $L_i$ and $R_i$ are both true:
    #     - $d_i = \text{Left} \implies$ visible
    #     - $d_i = \text{Right} \implies$ visible
    #     - (2 ways to be visible, 0 ways to be not visible)
    # - If $L_i$ is true and $R_i$ is false:
    #     - $d_i = \text{Left} \implies$ visible
    #     - $d_i = \text{Right} \implies$ not visible
    #     - (1 way to be visible, 1 way to be not visible)
    # - If $L_i$ is false and $R_i$ is true:
    #     - $d_i = \text{Left} \implies$ not visible
    #     - $d_i = \text{Right} \implies$ visible
    #     - (1 way to be visible, 1 way to be not visible)
    # - If $L_i$ is false and $R_i$ is false:
    #     - $d_i = \text{Left} \implies$ not visible
    #     - $d_i = \text{Right} \implies$ not visible
    #     - (0 ways to be visible, 2 ways to be not visible)

    # Let:
    # $c_2$ = count of $i$ where $L_i$ and $R_i$ are both true.
    # $c_1$ = count of $i$ where ($L_i$ xor $R_i$) is true.
    # $