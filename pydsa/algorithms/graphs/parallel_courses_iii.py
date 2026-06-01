METADATA = {
    "id": 2050,
    "name": "Parallel Courses III",
    "slug": "parallel_courses_iii",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "topological_sort", "dp", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n + e)",
    "space_complexity": "O(n + e)",
    "description": "Find the minimum number of semesters required to complete all courses given prerequisite constraints and individual course durations.",
}

from collections import deque

def solve(n: int, relations: list[list[int]], time: list[int]) -> int:
    """
    Calculates the minimum number of semesters needed to complete all courses.
    
    The problem is modeled as finding the longest path in a Directed Acyclic Graph (DAG),
    where nodes represent courses and edges represent prerequisite dependencies.
    The weight of the path is the sum of the 'time' values of the courses.

    Args:
        n: The total number of courses (labeled 1 to n).
        relations: A list of pairs [prevCourse, nextCourse] indicating dependencies.
        time: A list where time[i] is the duration of course i+1.

    Returns:
        The minimum number of semesters (total time) to complete all courses.

    Examples:
        >>> solve(3, [[1, 3], [2, 3]], [1, 2, 3])
        6
        >>> solve(3, [[1, 3], [2, 3]], [1, 1, 1])
        2
    """
    # Build adjacency list and in-degree array for topological sort
    adj: dict[int, list[int]] = {i: [] for i in range(1, n + 1)}
    in_degree: list[int] = [0] * (n + 1)
    
    for prev, next_course in relations:
        adj[prev].append(next_course)
        in_degree[next_course] += 1
        
    # dp[i] stores the earliest possible completion time for course i
    # Initialize with 0; we will update this as we traverse the DAG
    completion_time: list[int] = [0] * (n + 1)
    
    # Queue for Kahn's algorithm (topological sort)
    queue: deque[int] = deque()
    
    # Initialize queue with courses that have no prerequisites
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            # If no prerequisites, completion time is just the course duration
            completion_time[i] = time[i - 1]
            
    while queue:
        current = queue.popleft()
        
        for neighbor in adj[current]:
            # The earliest a neighbor can finish is its own time + 
            # the maximum completion time of all its prerequisites
            completion_time[neighbor] = max(
                completion_time[neighbor], 
                completion_time[current] + time[neighbor - 1]
            )
            
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    # The answer is the maximum completion time among all courses
    return max(completion_time)
