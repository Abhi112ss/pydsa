METADATA = {
    "id": 1633,
    "name": "Percentage of Users Attended a Contest",
    "slug": "percentage_of_users_attended_a_contest",
    "category": "hash_table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Compute the floor percentage of unique users who attended a contest.",
}


def solve() -> None:
    """Read input, compute the floor percentage of unique users who attended a contest,
    and print the result.

    Args:
        None. The function reads from standard input:
            - The first line contains an integer `total_users`.
            - The second line contains an integer `attendance_count`.
            - The third line contains `attendance_count` space‑separated integers
              representing user IDs that attended the contest.

    Returns:
        None. The function prints a single integer representing the floor
        percentage of unique attendees.

    Example:
        >>> # input
        >>> # 5
        >>> # 4
        >>> # 1 2 2 3
        >>> # output
        >>> # 60
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return

    # Parse total number of users
    total_users = int(data[0])

    # Parse number of attendance entries (may be omitted if not needed)
    if len(data) >= 2:
        attendance_count = int(data[1])
        attendance_start_index = 2
    else:
        attendance_count = 0
        attendance_start_index = 1

    # Extract user IDs; if attendance_count is larger than remaining tokens,
    # use all remaining tokens.
    user_id_strings = data[attendance_start_index : attendance_start_index + attendance_count]
    attended_user_ids = [int(uid) for uid in user_id_strings]

    # Count unique users using a hash set
    unique_attendees = set(attended_user_ids)

    # Compute floor percentage
    if total_users == 0:
        percentage = 0
    else:
        percentage = (len(unique_attendees) * 100) // total_users

    print(percentage)
