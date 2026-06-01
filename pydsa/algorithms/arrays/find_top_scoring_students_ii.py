METADATA = {
    "id": 3188,
    "name": "Find Top Scoring Students II",
    "slug": "find-top-scoring-students-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "array", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the names of students who have the highest scores, potentially involving multiple criteria or specific filtering.",
}

def solve(students: list[list[str | int]], k: int) -> list[str]:
    """
    Finds the top k students based on their scores. 
    In the context of this specific problem variation, we identify students 
    with the highest scores and return their names.

    Args:
        students: A list of lists where each sublist contains [name, score].
                  Note: name is str, score is int.
        k: The number of top students to retrieve (if applicable to the specific logic).

    Returns:
        A list of names of the top scoring students.

    Examples:
        >>> solve([["Alice", 100], ["Bob", 90], ["Charlie", 100]], 2)
        ['Alice', 'Charlie']
    """
    # Handle empty input case
    if not students:
        return []

    # Sort students primarily by score in descending order.
    # If scores are tied, the problem usually implies alphabetical order 
    # or maintaining original order; here we sort by score descending.
    # We use a lambda that negates the score for descending order.
    # To handle ties alphabetically, we can use ( -score, name ).
    sorted_students = sorted(
        students, 
        key=lambda x: (-int(x[1]), x[0])
    )

    # Identify the maximum score present in the list
    max_score = -1
    for student in sorted_students:
        score = int(student[1])
        if score > max_score:
            max_score = score
        else:
            # Since it's sorted, once we hit a lower score, we've seen the max
            break

    # Collect all names that have the maximum score
    top_students = []
    for student in sorted_students:
        name = str(student[0])
        score = int(student[1])
        
        if score == max_score:
            top_students.append(name)
        else:
            # Since the list is sorted by score descending, 
            # we can stop as soon as the score drops.
            break

    # If the problem asks for the top k students specifically:
    # return top_students[:k]
    # Based on the prompt's logic for "Find Top Scoring Students II":
    return top_students
