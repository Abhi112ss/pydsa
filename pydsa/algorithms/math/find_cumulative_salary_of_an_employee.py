METADATA = {
    "id": 579,
    "name": "Find Cumulative Salary of an Employee",
    "slug": "find-cumulative-salary-of-an-employee",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the cumulative salary of each employee for each month, excluding the last month.",
}

from typing import List, Dict


def solve(employee_table: List[Dict]) -> List[Dict]:
    """
    Calculates the cumulative salary of each employee for each month, 
    excluding the last month recorded for that employee.

    Args:
        employee_table: A list of dictionaries where each dictionary represents 
            a row in the 'Employee' table with keys 'id', 'month', and 'salary'.

    Returns:
        A list of dictionaries containing 'id', 'month', and 'salary' 
        representing the cumulative sum.

    Examples:
        >>> table = [
        ...     {"id": 1, "month": "Jan", "salary": 2000},
        ...     {"id": 1, "month": "Feb", "salary": 3000},
        ...     {"id": 1, "month": "Mar", "salary": 4000},
        ...     {"id": 2, "month": "Jan", "salary": 1000},
        ...     {"id": 2, "month": "Feb", "salary": 2000}
        ... ]
        >>> solve(table)
        [{'id': 1, 'month': 'Jan', 'salary': 2000}, {'id': 1, 'month': 'Feb', 'salary': 5000}, {'id': 2, 'month': 'Jan', 'salary': 1000}]
    """
    # Month order mapping to handle chronological sorting
    month_order = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    # Group data by employee ID
    employees_data: Dict[int, List[Dict]] = {}
    for row in employee_table:
        emp_id = row["id"]
        if emp_id not in employees_data:
            employees_data[emp_id] = []
        employees_data[emp_id].append(row)

    result: List[Dict] = []

    for emp_id, records in employees_data.items():
        # Sort records by month order to ensure cumulative sum is correct
        records.sort(key=lambda x: month_order[x["month"]])

        cumulative_sum = 0
        # We iterate through all records except the last one (as per problem requirement)
        # The last month's cumulative sum is not required in the output.
        for i in range(len(records) - 1):
            current_record = records[i]
            cumulative_sum += current_record["salary"]
            
            # Note: The problem asks for the cumulative salary UP TO that month.
            # In SQL terms: SUM(salary) OVER (PARTITION BY id ORDER BY month)
            # However, the cumulative sum for the current month includes the current month's salary.
            result.append({
                "id": emp_id,
                "month": current_record["month"],
                "salary": cumulative_sum
            })

    # The problem logic for cumulative sum usually implies:
    # Jan: 2000
    # Feb: 2000 + 3000 = 5000
    # But we must exclude the very last month of the sequence for each employee.
    
    # Re-calculating to match the exact cumulative logic:
    # The loop above actually calculates the sum including the current month.
    # Let's refine the logic to ensure it matches the expected output format.
    
    final_output: List[Dict] = []
    for emp_id, records in employees_data.items():
        records.sort(key=lambda x: month_order[x["month"]])
        
        running_total = 0
        # We need to output cumulative sums for all months except the last one.
        # For index i, the cumulative sum is sum(salary[0...i])
        for i in range(len(records)):
            running_total += records[i]["salary"]
            # If it's not the last month, add to result
            if i < len(records) - 1:
                final_output.append({
                    "id": emp_id,
                    "month": records[i]["month"],
                    "salary": running_total
                })
                
    # The requirement "excluding the last month" means if an employee has 3 months,
    # we output Jan and Feb.
    # Wait, the standard SQL solution for this is:
    # SELECT id, month, SUM(salary) OVER(PARTITION BY id ORDER BY month) as salary
    # FROM Employee
    # WHERE (id, month) NOT IN (SELECT id, MAX(month) FROM Employee GROUP BY id)
    
    # Let's re-verify the cumulative sum logic. 
    # If Jan=2000, Feb=3000, Mar=4000.
    # Cumulative: Jan=2000, Feb=5000, Mar=9000.
    # Exclude last: Jan=2000, Feb=5000.
    
    # The logic in the second loop of the function above is correct.
    # Let's clean up the function to return that.
    
    return _compute_correct_cumulative(employee_table, month_order)


def _compute_correct_cumulative(table: List[Dict], month_order: Dict[str, int]) -> List[Dict]:
    """Helper to perform the actual calculation logic."""
    employees_data: Dict[int, List[Dict]] = {}
    for row in table:
        emp_id = row["id"]
        if emp_id not in employees_data:
            employees_data[emp_id] = []
        employees_data[emp_id].append(row)

    final_result: List[Dict] = []
    
    for emp_id in employees_data:
        # Sort records chronologically
        records = sorted(employees_data[emp_id], key=lambda x: month_order[x["month"]])
        
        running_total = 0
        # Calculate cumulative sum for each month
        for i in range(len(records)):
            running_total += records[i]["salary"]
            # Append to result only if it's not the last month for this employee
            if i < len(records) - 1:
                final_result.append({
                    "id": emp_id,
                    "month": records[i]["month"],
                    "salary": running_total
                })
                
    return final_result
