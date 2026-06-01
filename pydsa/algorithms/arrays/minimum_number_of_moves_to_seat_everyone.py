METADATA = {
    "id": 2037,
    "name": "Minimum Number of Moves to Seat Everyone",
    "slug": "minimum-number-of-moves-to-seat-everyone",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum total distance to move people to available seats by pairing sorted positions.",
}

def solve(seats: list[int], students: list[int]) -> int:
    """
    Calculates the minimum number of moves required to seat all students.

    The optimal strategy is to sort both the seat positions and the student 
    positions and then pair the i-th smallest seat with the i-th smallest 
    student position. This greedy approach minimizes the total absolute 
    difference.

    Args:
        seats: A list of integers representing the positions of the seats.
        students: A list of integers representing the positions of the students.

    Returns:
        The minimum total number of moves (sum of absolute differences).

    Examples:
        >>> solve([3, 1, 5], [2, 7, 4])
        4
        >>> solve([1, 2, 3], [1, 2, 3])
        0
    """
    # Sort both lists to allow greedy pairing of the smallest available 
    # seat with the smallest available student position.
    seats.sort()
    students.sort()

    total_moves = 0
    
    # Iterate through the sorted lists and accumulate the absolute 
    # distance between each pair.
    for seat_pos, student_pos in zip(seats, students):
        total_moves += abs(seat_pos - student_pos)

    return total_moves
