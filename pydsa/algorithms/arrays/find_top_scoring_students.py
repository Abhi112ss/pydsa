METADATA = {
    "id": 3182,
    "name": "Find Top Scoring Students",
    "slug": "find-top-scoring-students",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all students who achieved the maximum score from a list of student-score pairs.",
}

def solve(students: list[list[str | int]]) -> list[str]:
    """
    Finds the names of all students who have the highest score.

    Args:
        students: A list of lists where each inner list contains a student's 
            name (str) and their score (int). Example: [["Alice", 90], ["Bob", 95]]

    Returns:
        A list of names (strings) of students who achieved the maximum score, 
        sorted lexicographically.

    Examples:
        >>> solve([["Alice", 90], ["Bob", 95], ["Charlie", 95]])
        ['Bob', 'Charlie']
        >>> solve([["Alice", 100], ["Bob", 100], ["Charlie", 100]])
        ['Alice', 'Bob', 'Charlie']
    """
    if not students:
        return []

    # Step 1: Find the maximum score present in the list
    # We iterate once to find the max value
    max_score = -1
    for _, score in students:
        if score > max_score:
            max_score = score

    # Step 2: Collect all names that match the maximum score
    top_students = []
    for name, score in students:
        if score == max_score:
            top_students.append(name)

    # Step 3: Sort the names lexicographically as per standard requirements
    # for such problems to ensure deterministic output
    top_students.sort()

    return top_students
