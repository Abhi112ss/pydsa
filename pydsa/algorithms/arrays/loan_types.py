METADATA = {
    "id": 2990,
    "name": "Loan Types",
    "slug": "loan_types",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Count the occurrences of each unique loan type in a given list.",
}

def solve(loan_types: list[str]) -> dict[str, int]:
    """
    Counts the frequency of each unique loan type in the provided list.

    Args:
        loan_types: A list of strings where each string represents a loan type.

    Returns:
        A dictionary where keys are the unique loan types and values are 
        their respective counts.

    Examples:
        >>> solve(["Personal", "Mortgage", "Personal", "Auto"])
        {'Personal': 2, 'Mortgage': 1, 'Auto': 1}
        >>> solve([])
        {}
    """
    # Initialize a dictionary to store the frequency of each loan type
    type_counts: dict[str, int] = {}

    for loan in loan_types:
        # If the loan type is already in the map, increment its count
        if loan in type_counts:
            type_counts[loan] += 1
        # Otherwise, initialize the count to 1
        else:
            type_counts[loan] = 1

    return type_counts
