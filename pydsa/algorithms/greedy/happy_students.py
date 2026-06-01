METADATA = {
    "id": 2860,
    "name": "Happy Students",
    "slug": "happy_students",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the number of students such that every student in the group has a grade at least 5 more than the minimum grade in the group.",
}

def solve(grades: list[int], k: int) -> int:
    """
    Finds the maximum number of students that can be chosen such that 
    the difference between the maximum and minimum grade in the group is at least 5.

    Args:
        grades: A list of integers representing student grades.
        k: The number of students to be selected (though the problem asks for 
           the maximum possible count, k is often used in variations; 
           here we find the maximum possible size of such a group).

    Returns:
        The maximum number of students that can form a 'happy' group.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
        6
        >>> solve([1, 2, 3, 4, 5], 0)
        0
    """
    # Sort grades to allow for a sliding window or two-pointer approach
    # to find the widest range that satisfies the condition.
    grades.sort()
    n = len(grades)
    max_students = 0

    # We iterate through every possible minimum grade in our group.
    # For a fixed minimum grade at index 'i', we need to find the 
    # smallest index 'j' such that grades[j] - grades[i] >= 5.
    # If such a 'j' exists, all students from index 'i' to 'j' 
    # (or any subset including i and j) could potentially form a group.
    # However, the problem asks for the maximum number of students 
    # where the condition (max - min >= 5) is met.
    # This means we pick a range [i, j] where grades[j] - grades[i] >= 5.
    # The number of students in this range is (j - i + 1).
    
    # Actually, the condition is: "every student in the group has a grade 
    # at least 5 more than the minimum grade in the group".
    # This implies: max(group) - min(group) >= 5.
    # To maximize the count, we want the largest range [i, j] 
    # such that grades[j] - grades[i] >= 5.
    
    right = 0
    for left in range(n):
        # Expand the right pointer until the condition is met
        while right < n and grades[right] - grades[left] < 5:
            right += 1
        
        # If we found a valid right pointer, the group size is (right - left + 1)
        # Wait, the condition is: "every student in the group has a grade 
        # at least 5 more than the minimum grade". 
        # This means if we pick index 'left' as the minimum, 
        # every other student 'x' in the group must satisfy grades[x] >= grades[left] + 5.
        # This is impossible if 'left' is part of the group unless the condition 
        # is interpreted as: there exists a subset where max - min >= 5.
        # Re-reading: "the difference between the maximum and minimum grade 
        # in the group is at least 5".
        
        # If grades[right] - grades[left] >= 5, then the group consisting 
        # of students from index 'left' to 'right' is NOT necessarily valid 
        # because the 'left' student themselves doesn't have a grade 5 more 
        # than the minimum (they ARE the minimum).
        
        # Correct interpretation: We need to pick a subset of students.
        # Let the minimum grade in our subset be G. 
        # Every other student in the subset must have grade >= G + 5.
        # To maximize the count, we pick one student with grade G, 
        # and ALL students with grade >= G + 5.
        
        # Let's find the first index 'j' such that grades[j] >= grades[left] + 5.
        # The number of students would be 1 (the student at 'left') 
        # + (number of students from index 'j' to n-1).
        
        # Reset right for each left to find the first valid j
        # (Optimization: 'right' only moves forward)
        if right < left:
            right = left
            
        while right < n and grades[right] < grades[left] + 5:
            right += 1
            
        if right < n:
            # Count = 1 (the min student) + all students from 'right' to end
            current_count = 1 + (n - right)
            if current_count > max_students:
                max_students = current_count

    return max_students
