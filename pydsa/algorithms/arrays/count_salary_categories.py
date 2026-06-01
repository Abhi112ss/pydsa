METADATA = {
    "id": 1907,
    "name": "Count Salary Categories",
    "slug": "count-salary-categories",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count how many employees fall into four specific salary categories based on predefined thresholds.",
}

def solve(salary: list[int]) -> list[list[str, int]]:
    """
    Categorizes salaries into four groups: 'Low Salary', 'Average Salary', 
    'High Salary', and 'Zero Salary'.

    Args:
        salary: A list of integers representing employee salaries.

    Returns:
        A list of lists, where each inner list contains a category name 
        and its corresponding count.

    Examples:
        >>> solve([2000, 3000, 4000, 10000, 200000])
        [['Low Salary', 2], ['Average Salary', 2], ['High Salary', 1], ['Zero Salary', 0]]
        >>> solve([0, 1000000])
        [['Low Salary', 0], ['Average Salary', 0], ['High Salary', 0], ['Zero Salary', 1]]
    """
    # Initialize counters for each category to ensure all categories are present in output
    counts = {
        "Low Salary": 0,
        "Average Salary": 0,
        "High Salary": 0,
        "Zero Salary": 0
    }

    for s in salary:
        # Categorize based on the problem constraints:
        # Zero Salary: s == 0
        # Low Salary: 0 < s < 20000
        # Average Salary: 20000 <= s <= 50000
        # High Salary: s > 50000
        if s == 0:
            counts["Zero Salary"] += 1
        elif s < 20000:
            counts["Low Salary"] += 1
        elif s <= 50000:
            counts["Average Salary"] += 1
        else:
            counts["High Salary"] += 1

    # Return the results in the specific order required by the problem
    return [
        ["Low Salary", counts["Low Salary"]],
        ["Average Salary", counts["Average Salary"]],
        ["High Salary", counts["High Salary"]],
        ["Zero Salary", counts["Zero Salary"]]
    ]
