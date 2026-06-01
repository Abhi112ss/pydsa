METADATA = {
    "id": 3051,
    "name": "Find Candidates for Data Scientist Position",
    "slug": "find_candidates_for_data_scientist_position",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(m)",
    "description": "Identify candidates who possess all the required skills for a specific position.",
}

def solve(required_skills: list[str], candidates: list[list[str]]) -> list[int]:
    """
    Finds the indices of candidates who possess all the required skills.

    Args:
        required_skills: A list of strings representing the skills needed.
        candidates: A list of lists, where each sub-list contains the skills of a candidate.

    Returns:
        A list of integers representing the indices of the qualifying candidates.

    Examples:
        >>> solve(["Python", "SQL"], [["Python", "SQL", "Java"], ["SQL"], ["Python", "SQL"]])
        [0, 2]
        >>> solve(["C++"], [["Java"], ["C++", "Python"]])
        [1]
    """
    # Convert required skills to a set for O(1) average time complexity lookups
    required_set = set(required_skills)
    qualifying_indices = []

    for index, candidate_skills in enumerate(candidates):
        # Convert current candidate's skills to a set
        candidate_set = set(candidate_skills)
        
        # Check if the required_set is a subset of the candidate_set
        # issubset() is efficient for checking if all elements of one set exist in another
        if required_set.issubset(candidate_set):
            qualifying_indices.append(index)

    return qualifying_indices
