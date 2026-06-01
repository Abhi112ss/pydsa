METADATA = {
    "id": 1494,
    "name": "Parallel Courses II",
    "slug": "parallel_courses_ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation", "graphs"],
    "difficulty": "hard",
    "time_complexity": "O(k * 2^n)",
    "space_complexity": "O(2^n)",
    "description": "Find the minimum number of semesters to complete all courses given a maximum number of courses per semester and prerequisite constraints.",
}

def solve(n: int, relations: list[list[int]], k: int) -> int:
    """
    Calculates the minimum number of semesters required to complete all courses.

    Args:
        n: The total number of courses (1-indexed).
        relations: A list of pairs [prevCourse, nextCourse] representing prerequisites.
        k: The maximum number of courses that can be taken in one semester.

    Returns:
        The minimum number of semesters to complete all courses. Returns -1 if impossible.

    Examples:
        >>> solve(3, [[1, 3], [2, 3]], 1)
        2
        >>> solve(3, [[1, 3], [2, 3]], 2)
        2
    """
    # Convert 1-indexed courses to 0-indexed for bitmasking
    # prereq_mask[i] stores a bitmask of all courses that must be completed before course i
    prereq_mask = [0] * n
    for prev, next_course in relations:
        prereq_mask[next_course - 1] |= (1 << (prev - 1))

    # dp[mask] stores the minimum semesters to reach the state represented by 'mask'
    # mask is a bitmask where the i-th bit is 1 if course i is completed
    target_mask = (1 << n) - 1
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    # Iterate through all possible states (subsets of completed courses)
    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue

        # Identify all courses that can be taken in the next semester
        # A course can be taken if it's not yet completed AND all its prerequisites are in the current mask
        available_courses_mask = 0
        for i in range(n):
            if not (mask & (1 << i)) and (prereq_mask[i] & mask) == prereq_mask[i]:
                available_courses_mask |= (1 << i)

        # If no courses are available but we haven't finished all, this path is invalid
        # (Though with valid DAG input, this shouldn't happen until target_mask is reached)
        if available_courses_mask == 0:
            continue

        # Extract indices of available courses to iterate through combinations
        available_indices = [i for i in range(n) if (available_courses_mask & (1 << i))]
        num_available = len(available_indices)

        # If we can take all available courses within the limit k
        if num_available <= k:
            new_mask = mask | available_courses_mask
            if dp[new_mask] > dp[mask] + 1:
                dp[new_mask] = dp[mask] + 1
        else:
            # If more than k courses are available, we must choose exactly k courses.
            # We use a sub-mask iteration or combinations to pick k courses from available_indices.
            # Since we want to find the minimum semesters, we try all combinations of size k.
            import itertools
            for combo in itertools.combinations(available_indices, k):
                new_mask = mask
                for idx in combo:
                    new_mask |= (1 << idx)
                
                if dp[new_mask] > dp[mask] + 1:
                    dp[new_mask] = dp[mask] + 1

    result = dp[target_mask]
    return int(result) if result != float('inf') else -1
