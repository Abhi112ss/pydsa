METADATA = {
    "id": 210,
    "name": "Course Schedule II",
    "slug": "course_schedule_ii",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "topological_sort", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Return the ordering of courses to finish all courses given prerequisites, or empty list if impossible.",
}


def solve(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """Find a valid ordering of courses using Kahn's algorithm (BFS topological sort).

    Args:
        num_courses: Total number of courses labeled 0..num_courses-1.
        prerequisites: List of [course, prerequisite] pairs.

    Returns:
        A valid ordering of courses, or empty list if a cycle exists.

    Examples:
        >>> solve(2, [[1, 0]])
        [0, 1]
        >>> solve(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        [0, 1, 2, 3]
        >>> solve(2, [[0, 1], [1, 0]])
        []
    """
    # Build adjacency list and in-degree count for each course.
    adjacency: dict[int, list[int]] = {course: [] for course in range(num_courses)}
    in_degree: dict[int, int] = {course: 0 for course in range(num_courses)}

    for course, prerequisite in prerequisites:
        adjacency[prerequisite].append(course)
        in_degree[course] += 1

    # Seed the queue with all courses that have no prerequisites.
    queue: list[int] = [course for course in range(num_courses) if in_degree[course] == 0]
    ordering: list[int] = []

    while queue:
        current = queue.pop(0)
        ordering.append(current)

        # Reduce in-degree of neighbors; enqueue any that become free.
        for neighbor in adjacency[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we couldn't visit every course, a cycle exists.
    return ordering if len(ordering) == num_courses else []