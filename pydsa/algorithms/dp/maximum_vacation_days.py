METADATA = {
    "id": 568,
    "name": "Maximum Vacation Days",
    "slug": "maximum-vacation-days",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(k * n^2)",
    "space_complexity": "O(k * n)",
    "description": "Find the maximum number of vacation days a person can have over k weeks given constraints on city transitions.",
}

def solve(vacation_days: list[list[int]], k: int) -> int:
    """
    Calculates the maximum number of vacation days possible over k weeks.

    Args:
        vacation_days: A 2D list where vacation_days[i][j] is the number of 
            vacation days in city j during week i.
        k: The total number of weeks to plan the vacation.

    Returns:
        The maximum total vacation days possible.

    Examples:
        >>> solve([[1, 1, 1], [1, 1, 1]], 2)
        2
        >>> solve([[1, 2, 3], [4, 5, 6]], 2)
        9
    """
    num_weeks = len(vacation_days)
    num_cities = len(vacation_days[0])

    # dp[w][c] represents the max vacation days ending at city 'c' in week 'w'
    # We use k weeks, but the input might have more or fewer weeks.
    # The problem implies we pick exactly k weeks. 
    # However, standard interpretation of such problems is choosing a sequence 
    # of k weeks from the available weeks. 
    # Given the constraints and typical LeetCode structure for this problem:
    # We assume we must pick k consecutive weeks or k weeks total? 
    # Re-reading: "Maximum vacation days over k weeks" usually implies 
    # we can pick any k weeks, but the transition constraint (cannot stay in 
    # the same city) applies to consecutive weeks in our selection.
    
    # If the problem implies we pick k weeks from the available 'num_weeks':
    # dp[i][j] = max vacation days using i weeks, ending in city j.
    
    dp = [[-1] * num_cities for _ in range(k + 1)]

    # Base case: Week 0 (no weeks chosen yet)
    # We initialize a dummy state or handle the first week separately.
    # Let's treat dp[i][j] as max days after choosing i weeks, with the i-th week being city j.
    
    # First week selection
    for city in range(num_cities):
        # We can pick any city in any week as our first week.
        # But usually, these problems imply we pick weeks in chronological order.
        # Let's assume we pick k weeks from the available weeks in order.
        pass

    # Correct DP approach for picking k weeks chronologically:
    # dp[i][w][c] = max days using i weeks, where the last week chosen was week 'w' and city 'c'.
    # This is O(k * num_weeks * num_cities).
    # If k is small and num_weeks is large, we use:
    # dp[i][c] = max days using i weeks, ending in city c.
    # To ensure chronological order, we need to track the last week index.
    
    # Let's refine: dp[i][w][c] is max days using i weeks, where the i-th week is week 'w' and city 'c'.
    # dp[i][w][c] = vacation_days[w][c] + max(dp[i-1][prev_w][prev_c]) 
    # where prev_w < w and prev_c != c.
    
    # Optimization: To avoid O(k * W^2 * C^2), we precalculate max values.
    # However, the constraint is prev_c != c.
    # For a fixed (i-1, prev_w), we only need the top 2 max values of dp[i-1][prev_w][prev_c]
    # with different cities to handle the prev_c != c constraint.

    # dp[i][w][c]
    # Since we only need i-1 to calculate i, we can optimize space to O(W * C)
    
    # current_dp[w][c] stores max days for 'i' weeks ending at week 'w', city 'c'
    current_dp = [[-1] * num_cities for _ in range(num_weeks)]

    # Base case: i = 1 (Choosing 1 week)
    for w in range(num_weeks):
        for c in range(num_cities):
            current_dp[w][c] = vacation_days[w][c]

    # Iterate for the remaining k-1 weeks
    for week_idx in range(2, k + 1):
        next_dp = [[-1] * num_cities for _ in range(num_weeks)]
        
        # Precompute the best and second best values from the previous 'i-1' weeks
        # to satisfy the prev_c != c constraint efficiently.
        # best_for_prev_w[w] = (max_val, city_index, second_max_val)
        best_for_prev_w = []
        for w in range(num_weeks):
            m1, c1, m2 = -1, -1, -1
            for c in range(num_cities):
                val = current_dp[w][c]
                if val > m1:
                    m2 = m1
                    m1 = val
                    c1 = c
                elif val > m2:
                    m2 = val
            best_for_prev_w.append((m1, c1, m2))

        # To find max(dp[i-1][prev_w][prev_c]) where prev_w < w and prev_c != c:
        # We can use a prefix maximum approach.
        # prefix_best[w] = max over all prev_w < w of (best_for_prev_w[prev_w])
        # This prefix_best needs to store the top 2 values with different cities.
        
        prefix_best = [] # List of (m1, c1, m2)
        curr_m1, curr_c1, curr_m2 = -1, -1, -1
        
        for w in range(num_weeks):
            prefix_best.append((curr_m1, curr_c1, curr_m2))
            # Update prefix best with the current week's bests for the next iteration
            m1, c1, m2 = best_for_prev_w[w]
            # Merge (m1, c1, m2) into (curr_m1, curr_c1, curr_m2)
            candidates = [(m1, c1), (m2, -1), (curr_m1, curr_c1), (curr_m2, -1)]
            # Sort candidates by value and pick top 2 unique cities
            candidates.sort(key=lambda x: x[0], reverse=True)
            
            new_m1, new_c1, new_m2 = -1, -1, -1
            for val, city in candidates:
                if val == -1: continue
                if new_c1 == -1:
                    new_m1, new_c1 = val, city
                elif city != new_c1 and val > new_m2:
                    new_m2 = val
            curr_m1, curr_c1, curr_m2 = new_m1, new_c1, new_m2

        # Now fill next_dp
        for w in range(num_weeks):
            for c in range(num_cities):
                # Find best prev_w < w such that prev_c != c
                m1, c1, m2 = prefix_best[w]
                best_prev_val = m1 if c1 != c else m2
                
                if best_prev_val != -1:
                    next_dp[w][c] = vacation_days[w][c] + best_prev_val
        
        current_dp = next_dp

    # The answer is the max value in the current_dp table
    ans = -1
    for w in range(num_weeks):
        for c in range(num_cities):
            ans = max(ans, current_dp[w][c])
            
    return ans
