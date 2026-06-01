METADATA = {
    "id": 1109,
    "name": "Corporate Flight Bookings",
    "slug": "corporate-flight-bookings",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "arrays", "difference_array"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Given n flights and a list of bookings, return the total number of seats booked for each flight.",
}

def solve(n: int, bookings: list[list[int]]) -> list[int]:
    """
    Calculates the total number of seats booked for each flight using a difference array.

    Args:
        n: The number of flights.
        bookings: A list of bookings where each booking is [first, last, seats].
                  The flight indices are 1-indexed.

    Returns:
        A list of integers representing the total seats booked for each flight.

    Examples:
        >>> solve(5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]])
        [10, 55, 45, 25, 25]
        >>> solve(3, [[1, 3, 10]])
        [10, 10, 10]
    """
    # Initialize a difference array of size n + 1 to handle boundary conditions easily.
    # We use n + 1 to allow index 'last' to be used without immediate bounds checking.
    diff_array = [0] * (n + 1)

    for first, last, seats in bookings:
        # Convert 1-based indexing to 0-based indexing.
        # Increment the start of the range.
        diff_array[first - 1] += seats
        
        # Decrement the element immediately after the end of the range.
        if last < n:
            diff_array[last] -= seats

    # Compute the prefix sum to transform the difference array into the actual counts.
    # The value at index i is the sum of all differences from 0 to i.
    result = [0] * n
    current_sum = 0
    for i in range(n):
        current_sum += diff_array[i]
        result[i] = current_sum

    return result
