METADATA = {
    "id": 1661,
    "name": "Average Time of Process per Machine",
    "slug": "average_time_of_process_per_machine",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "aggregation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Compute average processing time per machine from start and end timestamps.",
}


def solve(processes: list[list[int]]) -> list[list[int]]:
    """Calculate the average processing time for each machine.

    Args:
        processes: A list of records where each record is a list of three integers:
            [machine_id, start_time, end_time].

    Returns:
        A list of [machine_id, average_time] pairs sorted by machine_id.
        The average_time is the ceiling of the arithmetic mean of (end_time - start_time)
        for all processes belonging to the same machine.

    Examples:
        >>> solve([[1, 0, 5], [2, 1, 3], [1, 2, 8]])
        [[1, 6], [2, 2]]
        >>> solve([[3, 10, 15], [3, 20, 25], [4, 5, 7]])
        [[3, 6], [4, 2]]
    """
    # Dictionaries to accumulate total duration and count per machine.
    total_duration_by_machine: dict[int, int] = {}
    count_by_machine: dict[int, int] = {}

    for record in processes:
        machine_id, start_time, end_time = record
        duration = end_time - start_time
        # Update aggregates.
        total_duration_by_machine[machine_id] = total_duration_by_machine.get(machine_id, 0) + duration
        count_by_machine[machine_id] = count_by_machine.get(machine_id, 0) + 1

    # Build result list with ceiling division for average.
    result: list[list[int]] = []
    for machine_id in total_duration_by_machine:
        total = total_duration_by_machine[machine_id]
        count = count_by_machine[machine_id]
        average_time = (total + count - 1) // count  # ceiling division
        result.append([machine_id, average_time])

    # Return results sorted by machine_id.
    result.sort(key=lambda pair: pair[0])
    return result