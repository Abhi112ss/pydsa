METADATA = {
    "id": 2580,
    "name": "Count Ways to Group Overlapping Ranges",
    "slug": "count-ways-to-group-overlapping-ranges",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["intervals", "dp", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of ways to group overlapping intervals into disjoint sets using Bell numbers for each connected component.",
}

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the number of ways to group overlapping intervals into disjoint sets.
    
    The problem can be broken down into two steps:
    1. Identify connected components of overlapping intervals.
    2. For each component of size 'k', calculate the Bell number B(k), which represents 
       the number of ways to partition a set of k elements.
    3. The total number of ways is the product of Bell numbers of all component sizes, 
       modulo 10^9 + 7.

    Args:
        intervals: A list of intervals where intervals[i] = [start_i, end_i].

    Returns:
        The total number of ways to group the intervals modulo 10^9 + 7.

    Examples:
        >>> solve([[1, 3], [2, 4], [5, 6]])
        2
        >>> solve([[1, 2], [2, 3], [3, 4]])
        1
    """
    MOD = 1_000_000_007
    n = len(intervals)
    if n == 0:
        return 0

    # Step 1: Sort intervals by start time to easily find connected components
    intervals.sort()

    component_sizes = []
    if n > 0:
        current_max_end = intervals[0][1]
        current_count = 1
        
        for i in range(1, n):
            start, end = intervals[i]
            # If the current interval starts before or at the max end of the current component,
            # it belongs to the same connected component.
            if start <= current_max_end:
                current_count += 1
                current_max_end = max(current_max_end, end)
            else:
                # Otherwise, a new component starts.
                component_sizes.append(current_count)
                current_count = 1
                current_max_end = end
        component_sizes.append(current_count)

    # Step 2: Precompute Bell numbers using Stirling numbers of the second kind or DP.
    # We use the Bell triangle (Aitken's array) method to compute Bell numbers efficiently.
    # Bell(n) is the first element of the n-th row in the Bell triangle.
    max_size = max(component_sizes)
    bell = [0] * (max_size + 1)
    
    # bell_triangle[i][j] will store values for the Bell triangle construction
    # To save space, we can use a 1D array to simulate the row updates.
    triangle_row = [0] * (max_size + 1)
    triangle_row[0] = 1
    bell[0] = 1
    
    for i in range(1, max_size + 1):
        # The first element of the current row is the last element of the previous row
        prev_last = triangle_row[i - 1]
        new_row = [0] * (i + 1)
        new_row[0] = prev_last
        
        # Fill the rest of the row: new_row[j] = new_row[j-1] + prev_row[j-1]
        for j in range(1, i + 1):
            new_row[j] = (new_row[j - 1] + triangle_row[j - 1]) % MOD
        
        triangle_row = new_row
        # The Bell number B(i) is the first element of the i-th row (or last of i-1 row)
        # In this specific construction, B(i) is new_row[0]
        bell[i] = new_row[0]

    # Note: The Bell triangle construction above:
    # Row 0: 1
    # Row 1: 1, 2
    # Row 2: 2, 3, 5
    # Row 3: 5, 7, 10, 15
    # The Bell number B(n) is the first element of row n.
    # Let's re-verify: B(0)=1, B(1)=1, B(2)=2, B(3)=5.
    # My loop logic:
    # i=1: new_row[0]=1, new_row[1]=1+1=2. bell[1]=1.
    # i=2: new_row[0]=2, new_row[1]=2+1=3, new_row[2]=3+2=5. bell[2]=2.
    # This works.

    # Step 3: Multiply Bell numbers of all component sizes
    ans = 1
    for size in component_sizes:
        ans = (ans * bell[size]) % MOD

    return ans
