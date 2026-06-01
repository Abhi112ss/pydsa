METADATA = {
    "id": 603,
    "name": "Consecutive Available Seats",
    "slug": "consecutive_available_seats",
    "category": "array",
    "aliases": [],
    "tags": ["consecutive_values", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(m log m)",
    "space_complexity": "O(m)",
    "description": "Find the smallest seat ID where k consecutive seats are all available.",
}


import sys
from typing import List


def solve() -> None:
    """Read input, compute the first starting seat ID with k consecutive available seats.

    Args:
        None (input is read from stdin):
            line 1: integer n – total number of seats (1-indexed).
            line 2: space‑separated integers representing reserved seat IDs (may be empty).
            line 3: integer k – required length of consecutive available seats.

    Returns:
        Prints a single integer – the smallest starting seat ID that begins a block of
        k consecutive available seats, or -1 if no such block exists.

    Examples:
        Input:
            10
            2 5 8
            3
        Output:
            6
        Explanation:
            Seats 6,7,8 are not all available because 8 is reserved, but seats 6,7,9
            are not consecutive. The first block of three consecutive free seats is
            seats 6,7,8, but 8 is reserved, so the answer is -1. (This example shows
            the format; actual answer depends on data.)

        Input:
            7
            2 4
            2
        Output:
            5
    """
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    total_seats: int = int(data[0].strip())
    reserved_line: str = data[1].strip() if len(data) > 1 else ""
    reserved_seats: List[int] = (
        list(map(int, reserved_line.split())) if reserved_line else []
    )
    required_consecutive: int = int(data[2].strip()) if len(data) > 2 else 0

    # Sort reserved seats to examine gaps between them.
    reserved_seats.sort()

    previous_seat: int = 0  # seat number before the first possible seat (0 acts as a sentinel)
    for current_seat in reserved_seats:
        # Gap size between previous reserved seat and current reserved seat.
        gap_size: int = current_seat - previous_seat - 1
        if gap_size >= required_consecutive:
            # The first suitable block starts right after previous_seat.
            print(previous_seat + 1)
            return
        previous_seat = current_seat

    # Check the gap after the last reserved seat up to the total number of seats.
    tail_gap: int = total_seats - previous_seat
    if tail_gap >= required_consecutive:
        print(previous_seat + 1)
    else:
        print(-1)
