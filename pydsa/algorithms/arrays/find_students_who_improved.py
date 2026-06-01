METADATA = {
    "id": 3421,
    "name": "Find Students Who Improved",
    "slug": "find-students-who-improved",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "comparison"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Identify students whose scores in the current term are strictly greater than their scores in the previous term.",
}

def solve(scores: list[list[int]]) -> list[int]:
    """
    Identifies the indices of students who showed improvement in their scores.

    A student is considered to have improved if their score in the current term 
    (the last element in their score list) is strictly greater than their score 
    in the previous term (the second to last element).

    Args:
        scores: A list of lists, where each inner list contains the scores 
            of a student across multiple terms. Each inner list has at least 
            two elements.

    Returns:
        A list of integers representing the indices of the students who improved.

    Examples:
        >>> solve([[10, 15], [20, 20], [5, 10]])
        [0, 2]
        >>> solve([[10, 5], [10, 10], [1, 2]])
        [2]
    """
    improved_students = []
    
    # Iterate through each student's score history using their index
    for student_index, student_scores in enumerate(scores):
        # The problem implies comparing the most recent term with the one immediately preceding it
        # We access the last element and the second to last element
        current_term_score = student_scores[-1]
        previous_term_score = student_scores[-2]
        
        # Check if the score has strictly increased
        if current_term_score > previous_term_score:
            improved_students.append(student_index)
            
    return improved_students
