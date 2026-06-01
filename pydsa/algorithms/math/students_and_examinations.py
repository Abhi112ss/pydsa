METADATA = {
    "id": 1280,
    "name": "Students and Examinations",
    "slug": "students-and-examinations",
    "category": "Database",
    "aliases": [],
    "tags": ["counting", "logic", "sql-logic"],
    "difficulty": "easy",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N * M)",
    "description": "Find the number of times each student attended each exam, including zero counts.",
}

from collections import Counter

def solve(students: list[dict], subjects: list[dict], examinations: list[dict]) -> list[dict]:
    """
    Calculates the number of times each student attended each exam.
    
    The result includes all combinations of students and subjects, even if 
    the student attended zero exams for a specific subject.

    Args:
        students: A list of dictionaries where each dict contains 'student_id' and 'student_name'.
        subjects: A list of dictionaries where each dict contains 'subject_name'.
        examinations: A list of dictionaries where each dict contains 'student_id' and 'subject_name'.

    Returns:
        A list of dictionaries sorted by student_id and subject_name, containing 
        'student_id', 'student_name', 'subject_name', and 'attended_exams'.

    Examples:
        >>> students = [{"student_id": 1, "student_name": "Alice"}, {"student_id": 2, "student_name": "Bob"}]
        >>> subjects = [{"subject_name": "Math"}, {"subject_name": "Physics"}]
        >>> examinations = [{"student_id": 1, "subject_name": "Math"}]
        >>> solve(students, subjects, examinations)
        [{'student_id': 1, 'student_name': 'Alice', 'subject_name': 'Math', 'attended_exams': 1}, 
         {'student_id': 1, 'student_name': 'Alice', 'subject_name': 'Physics', 'attended_exams': 0}, 
         {'student_id': 2, 'student_name': 'Bob', 'subject_name': 'Math', 'attended_exams': 0}, 
         {'student_id': 2, 'student_name': 'Bob', 'subject_name': 'Physics', 'attended_exams': 0}]
    """
    # Create a frequency map of (student_id, subject_name) pairs from examinations
    # This allows O(1) lookup for the count of each specific student-subject pair
    exam_counts = Counter()
    for exam in examinations:
        exam_counts[(exam["student_id"], exam["subject_name"])] += 1

    results = []

    # Iterate through every student to ensure they are included in the output
    for student in students:
        student_id = student["student_id"]
        student_name = student["student_name"]
        
        # Perform a Cartesian product with all subjects to ensure every 
        # student-subject combination is represented
        for subject in subjects:
            subject_name = subject["subject_name"]
            
            # Retrieve the count from our frequency map, defaulting to 0 if not found
            attended_count = exam_counts.get((student_id, subject_name), 0)
            
            results.append({
                "student_id": student_id,
                "student_name": student_name,
                "subject_name": subject_name,
                "attended_exams": attended_count
            })

    # Sort the results by student_id and then by subject_name as per problem requirements
    results.sort(key=lambda x: (x["student_id"], x["subject_name"]))
    
    return results
