METADATA = {
    "id": 1452,
    "name": "People Whose List of Favorite Companies Is Not a Subset of Another List",
    "slug": "people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_set", "string", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 * m)",
    "space_complexity": "O(n * m)",
    "description": "Find all people whose list of favorite companies is not a subset of any other person's list.",
}

def solve(favoriteCompanies: list[list[str]]) -> list[int]:
    """
    Identifies indices of people whose favorite companies list is not a subset 
    of any other person's list.

    Args:
        favoriteCompanies: A list of lists, where each inner list contains 
            strings representing favorite companies of a person.

    Returns:
        A list of integers representing the indices of people who satisfy the condition.

    Examples:
        >>> solve([["a","b"],["a"],["b"]])
        [0]
        >>> solve([["a","b"],["a","b","c"],["a","b","c"]])
        [0]
    """
    n = len(favoriteCompanies)
    # Convert each list to a set for O(1) average time complexity lookups 
    # and efficient subset operations.
    company_sets = [set(companies) for companies in favoriteCompanies]
    
    result_indices = []

    for i in range(n):
        is_subset = False
        for j in range(n):
            # A person's list cannot be a subset of itself in this context 
            # (we are looking for a DIFFERENT person's list).
            if i == j:
                continue
            
            # Check if company_sets[i] is a subset of company_sets[j].
            # The issubset method is highly optimized in Python.
            if company_sets[i].issubset(company_sets[j]):
                is_subset = True
                break
        
        # If we checked all other people and found no superset, add index to result.
        if not is_subset:
            result_indices.append(i)
            
    return result_indices
