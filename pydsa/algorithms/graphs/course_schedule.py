METADATA = {
    "id": 207,
    "name": "Course Schedule",
    "slug": "course-schedule",
    "category": "Graphs",
    "aliases": [],
    "tags": ["dfs", "bfs", "topological_sort", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Determine if it is possible to finish all courses given a set of prerequisite dependencies.",
}

def solve(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Args:
        num_courses: The total number of courses.
        prerequisites: A list of pairs where [a, b] means course b must be taken before course a.

    Returns:
        True if all courses can be finished, False otherwise.
    """
    adj_list = [[] for _ in range(num_courses)]
    in_degree = [0] * num_courses

    for course, pre in prerequisites:
        adj_list[pre].append(course)
        in_degree[course] += 1

    queue = []
    for i in range(num_courses):
        if in_degree[i] == 0:
            queue.append(i)

    processed_courses_count = 0
    head_index = 0
    while head_index < len(queue):
        current_course = queue[head_index]
        head_index += 1
        processed_courses_count += 1

        for neighbor in adj_list[current_course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return processed_courses_count == num_courses