METADATA = {
    "id": 1077,
    "name": "Project Employees III",
    "slug": "project-employees-iii",
    "category": "Array",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Calculate the sum of maximum experience years for employees in each project, considering only those with the highest experience in that project.",
}

def solve(experience: list[int], project: list[int], employee: list[int]) -> list[int]:
    """
    Calculates the sum of maximum experience years for employees in each project.
    
    For each project, we identify the maximum experience level among its employees.
    The result for that project is the sum of the experience levels of all employees 
    in that project who possess that maximum experience level.

    Args:
        experience: A list of integers representing the experience years of each employee.
        project: A list of integers where project[i] is the project ID for employee[i].
        employee: A list of integers where employee[i] is the employee ID for index i.
        
    Note: The problem description implies a mapping between employee IDs and experience.
    Based on standard LeetCode constraints for this type of problem, we assume 
    the input lists are aligned by index.

    Returns:
        A list of integers representing the sum of max experience for each project, 
        sorted by project ID.

    Examples:
        >>> solve([1, 2, 3], [1, 1, 2], [1, 2, 3])
        [3, 3]
    """
    # Map to store: project_id -> max_experience_found_so_far
    project_max_exp: dict[int, int] = {}
    # Map to store: project_id -> sum_of_max_experience_employees
    project_sum_exp: dict[int, int] = {}
    
    # First pass: Find the maximum experience for each project
    for i in range(len(experience)):
        exp = experience[i]
        proj = project[i]
        
        if proj not in project_max_exp or exp > project_max_exp[proj]:
            project_max_exp[proj] = exp
            
    # Second pass: Sum the experience of employees matching the max experience for their project
    for i in range(len(experience)):
        exp = experience[i]
        proj = project[i]
        
        # If this employee's experience matches the max found for this project
        if exp == project_max_exp[proj]:
            project_sum_exp[proj] = project_sum_exp.get(proj, 0) + exp
            
    # Get all unique project IDs and sort them to return results in order
    sorted_project_ids = sorted(project_max_exp.keys())
    
    return [project_sum_exp[pid] for pid in sorted_project_ids]
