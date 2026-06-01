METADATA = {
    "id": 1075,
    "name": "Project Employees I",
    "slug": "project-employees-i",
    "category": "SQL/Algorithm Simulation",
    "aliases": [],
    "tags": ["math", "arrays", "grouping"],
    "difficulty": "easy",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N)",
    "description": "Calculate the average years of experience for each project by joining employee and project data.",
}

from typing import Any, Dict, List


def solve(employee_table: List[Dict[str, Any]], project_table: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Calculates the average years of experience for each project.

    Args:
        employee_table: A list of dictionaries where each dict represents an employee
            with keys 'employee_id' and 'experience_years'.
        project_table: A list of dictionaries where each dict represents a project
            mapping with keys 'project_id' and 'employee_id'.

    Returns:
        A list of dictionaries containing 'project_id' and 'average_years' (rounded to 2 decimals).

    Examples:
        >>> emp = [{'employee_id': 1, 'experience_years': 3}, {'employee_id': 2, 'experience_years': 1}]
        >>> proj = [{'project_id': 1, 'employee_id': 1}, {'project_id': 1, 'employee_id': 2}]
        >>> solve(emp, proj)
        [{'project_id': 1, 'average_years': 2.0}]
    """
    # Step 1: Create a lookup map for employee experience for O(1) access
    # This simulates the join operation efficiency
    experience_map: Dict[int, int] = {
        emp["employee_id"]: emp["experience_years"] 
        for emp in employee_table
    }

    # Step 2: Aggregate experience years and counts per project
    # project_stats will store {project_id: [sum_experience, count]}
    project_stats: Dict[int, List[float]] = {}

    for entry in project_table:
        project_id = entry["project_id"]
        employee_id = entry["employee_id"]
        
        # Get experience from our lookup map
        years = experience_map.get(employee_id, 0)

        if project_id not in project_stats:
            project_stats[project_id] = [0.0, 0.0]
        
        project_stats[project_id][0] += years
        project_stats[project_id][1] += 1

    # Step 3: Compute the mean and format the result
    results: List[Dict[str, Any]] = []
    # Sort by project_id to ensure deterministic output if required
    for project_id in sorted(project_stats.keys()):
        total_years, count = project_stats[project_id]
        average_years = round(total_years / count, 2)
        results.append({
            "project_id": project_id,
            "average_years": average_years
        })

    return results
