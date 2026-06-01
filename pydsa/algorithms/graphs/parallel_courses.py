METADATA = {
    "id": 1136,
    "name": "Parallel Courses",
    "slug": "parallel_courses",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "topological_sort", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Determine the minimum number of semesters required to complete all courses given their prerequisites.",
}

from collections import deque

def solve(n: int, relations: list[list[int]]) -> int:
    """
    Calculates the minimum number of semesters needed to complete all courses.
    
    Uses Kahn's algorithm (BFS-based topological sort) to process courses level by level.
    Each level in the BFS represents one semester.

    Args:
        n: The total number of courses (labeled 1 to n).
        relations: A list of pairs [prevCourse, nextCourse] indicating prerequisites.

    Returns:
        The minimum number of semesters required, or -1 if it is impossible to 
        complete all courses due to a cycle.

    Examples:
        >>> solve(3, [[1, 3], [2, 3]])
        2
        >>> solve(3, [[1, 2], [2, 3], [3, 1]])
        -1
    """
    # Build adjacency list and in-degree array
    # Courses are 1-indexed, so we use size n + 1
    adj_list: dict[int, list[int]] = {i: [] for i in range(1, n + 1)}
    in_degree: list[int] = [0] * (n + 1)

    for prev, next_course in relations:
        adj_list[prev].append(next_course)
        in_degree[next_course] += 1

    # Initialize queue with all courses that have no prerequisites
    queue: deque[int] = deque()
    for course in range(1, n + 1):
        if in_degree[course] == 0:
            queue.append(course)

    semesters_count = 0
    courses_completed = 0

    # Process courses level by level (each level is one semester)
    while queue:
        semesters_count += 1
        # The number of courses available to take this semester
        courses_this_semester = len(queue)
        courses_completed += courses_this_semester

        for _ in range(courses_this_semester):
            current_course = queue.popleft()

            for neighbor in adj_list[current_course]:
                in_degree[neighbor] -= 1
                # If all prerequisites for the neighbor are met, add to next semester
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    # If we couldn't complete all courses, there must be a cycle
    return semesters_count if courses_completed == n else -1
