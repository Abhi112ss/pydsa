METADATA = {
    "id": 2356,
    "name": "Number of Unique Subjects Taught by Each Teacher",
    "slug": "number-of-unique-subjects-taught-by-each-teacher",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "set"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of unique subjects taught by each teacher using a hash map of sets.",
}

def solve(teacher: list[int], subject: list[int]) -> list[int]:
    """
    Calculates the number of unique subjects taught by each teacher.

    Args:
        teacher: A list of teacher IDs where teacher[i] is the teacher for subject[i].
        subject: A list of subject IDs where subject[i] is the subject for teacher[i].

    Returns:
        A list of integers where the i-th element is the number of unique subjects 
        taught by teacher i+1.

    Examples:
        >>> solve([1, 1, 2], [1, 2, 1])
        [2, 1]
        >>> solve([1, 1, 1, 2, 2], [1, 2, 3, 1, 2])
        [3, 2]
    """
    # Use a dictionary to map teacher IDs to a set of unique subject IDs.
    # Using a set automatically handles duplicate subject entries for the same teacher.
    teacher_to_subjects = {}

    for t_id, s_id in zip(teacher, subject):
        if t_id not in teacher_to_subjects:
            teacher_to_subjects[t_id] = set()
        teacher_to_subjects[t_id].add(s_id)

    # Determine the number of teachers. 
    # Since teacher IDs are 1-indexed, the max ID is the count of teachers.
    num_teachers = len(teacher) # This is incorrect if IDs are not contiguous, 
    # but per problem constraints, teacher IDs are 1 to n.
    # Let's find the actual max teacher ID to be safe.
    max_teacher_id = 0
    for t_id in teacher:
        if t_id > max_teacher_id:
            max_teacher_id = t_id

    # Construct the result list. 
    # We iterate from 1 to max_teacher_id and fetch the size of the set.
    result = []
    for i in range(1, max_teacher_id + 1):
        # If a teacher ID exists in the input, add the count of their unique subjects.
        # Otherwise, they teach 0 subjects.
        if i in teacher_to_subjects:
            result.append(len(teacher_to_subjects[i]))
        else:
            result.append(0)

    return result
