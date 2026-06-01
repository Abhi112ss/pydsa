METADATA = {
    "id": 3057,
    "name": "Employees Project Allocation",
    "slug": "employees-project-allocation",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "backtracking", "matching", "bipartite matching"],
    "difficulty": "medium",
    "time_complexity": "O(V * E)",
    "space_complexity": "O(V + E)",
    "description": "Allocate employees to projects such that each employee is assigned to at most one project and each project is assigned to at most one employee, maximizing the total number of assignments.",
}

def solve(employees_skills: list[list[int]], project_requirements: list[list[int]]) -> int:
    """
    Calculates the maximum number of employees that can be assigned to projects.
    
    An employee can be assigned to a project if the employee's skills 
    contain all the required skills for that project. Each employee and 
    each project can be used at most once.

    Args:
        employees_skills: A list of lists where each sublist contains the skill IDs of an employee.
        project_requirements: A list of lists where each sublist contains the skill IDs required for a project.

    Returns:
        The maximum number of successful employee-to-project assignments.

    Examples:
        >>> solve([[1, 2], [3]], [[1], [2], [3]])
        2
        >>> solve([[1], [2]], [[1, 2]])
        0
    """
    num_employees = len(employees_skills)
    num_projects = len(project_requirements)

    # Pre-process skills into sets for O(1) average lookup
    employee_skill_sets = [set(skills) for skills in employees_skills]
    project_requirement_sets = [set(reqs) for reqs in project_requirements]

    # Build adjacency list: adj[i] contains indices of projects employee i can handle
    adj = [[] for _ in range(num_employees)]
    for emp_idx in range(num_employees):
        for proj_idx in range(num_projects):
            # Check if employee has all required skills for the project
            if project_requirement_sets[proj_idx].issubset(employee_skill_sets[emp_idx]):
                adj[emp_idx].append(proj_idx)

    # match_project[p] stores the index of the employee assigned to project p, or -1
    match_project = [-1] * num_projects
    total_matches = 0

    def can_match(emp_idx: int, visited_projects: list[bool]) -> bool:
        """DFS to find an augmenting path for the given employee."""
        for proj_idx in adj[emp_idx]:
            if not visited_projects[proj_idx]:
                visited_projects[proj_idx] = True
                
                # If project is unassigned OR the current occupant can be reassigned
                if match_project[proj_idx] < 0 or can_match(match_project[proj_idx], visited_projects):
                    match_project[proj_idx] = emp_idx
                    return True
        return False

    # Iterate through each employee to attempt an assignment
    for emp_idx in range(num_employees):
        # visited_projects tracks projects visited in the current DFS traversal
        visited_projects = [False] * num_projects
        if can_match(emp_idx, visited_projects):
            total_matches += 1

    return total_matches
