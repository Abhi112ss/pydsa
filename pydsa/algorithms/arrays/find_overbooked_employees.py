METADATA = {
    "id": 3611,
    "name": "Find Overbooked Employees",
    "slug": "find-overbooked-employees",
    "category": "Intervals",
    "aliases": [],
    "tags": ["sorting", "sweep_line", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Identify employees who are overbooked by finding if any time intervals overlap.",
}

def solve(schedules: list[list[list[int]]]) -> list[int]:
    """
    Args:
        schedules: A list of lists where each sub-list contains the [start, end] intervals for an employee.

    Returns:
        A list of employee indices who have overlapping intervals.
    """
    overbooked_employees = set()
    events = []

    for employee_index, intervals in enumerate(schedules):
        for start, end in intervals:
            events.append((start, 1, employee_index))
            events.append((end, -1, employee_index))

    events.sort(key=lambda x: (x[0], x[1]))

    active_employees = {}

    for time, type_delta, employee_index in events:
        if type_delta == 1:
            if employee_index in active_employees:
                overbooked_employees.add(employee_index)
            active_employees[employee_index] = active_employees.get(employee_index, 0) + 1
        else:
            active_employees[employee_index] -= 1
            if active_employees[employee_index] == 0:
                del active_employees[employee_index]

    for employee_index, intervals in enumerate(schedules):
        if len(intervals) <= 1:
            continue
        
        sorted_intervals = sorted(intervals)
        for i in range(len(sorted_intervals) - 1):
            if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
                overbooked_employees.add(employee_index)
                break

    final_overbooked = []
    for employee_index, intervals in enumerate(schedules):
        if len(intervals) > 1:
            sorted_intervals = sorted(intervals)
            has_overlap = False
            for i in range(len(sorted_intervals) - 1):
                if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
                    has_overlap = True
                    break
            if has_overlap:
                final_overbooked.append(employee_index)
        elif employee_index in overbooked_employees:
            final_overbooked.append(employee_index)

    result = []
    for i in range(len(schedules)):
        intervals = sorted(schedules[i])
        is_overbooked = False
        for j in range(len(intervals) - 1):
            if intervals[j][1] > intervals[j+1][0]:
                is_overbooked = True
                break
        if is_overbooked:
            result.append(i)
            
    return result