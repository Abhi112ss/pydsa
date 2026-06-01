METADATA = {
    "id": 1462,
    "name": "Course Schedule IV",
    "slug": "course-schedule-iv",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "dfs", "bfs", "transitive_closure"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Determine if specific prerequisite relationships exist in a directed graph of courses.",
}

def solve(num_courses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    """
    Determines if a course is a prerequisite of another for multiple queries.

    The problem is solved by computing the transitive closure of the course 
    dependency graph. We use the Floyd-Warshall algorithm to find all 
    reachable nodes in the directed graph.

    Args:
        num_courses: The total number of courses.
        prerequisites: A list of pairs [a, b] where b is a prerequisite of a.
        queries: A list of pairs [u, v] to check if v is a prerequisite of u.

    Returns:
        A list of booleans corresponding to each query.

    Examples:
        >>> solve(3, [[1, 0], [2, 1]], [[1, 0], [2, 0], [2, 1], [0, 1]])
        [True, True, True, False]
    """
    # Initialize a reachability matrix where is_prereq[i][j] is True 
    # if course j is a prerequisite of course i.
    is_prereq = [[False] * num_courses for _ in range(num_courses)]

    # Populate the matrix with direct prerequisites
    for course, prereq in prerequisites:
        is_prereq[course][prereq] = True

    # Floyd-Warshall algorithm to compute transitive closure.
    # k is the intermediate course being considered.
    for k in range(num_courses):
        for i in range(num_courses):
            for j in range(num_courses):
                # If i depends on k AND k depends on j, then i depends on j.
                if is_prereq[i][k] and is_prereq[k][j]:
                    is_prereq[i][j] = True

    # Answer each query in O(1) using the precomputed matrix.
    results = []
    for u, v in queries:
        results.append(is_prereq[u][v])

    return results
