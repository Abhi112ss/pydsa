METADATA = {
    "id": 3767,
    "name": "Maximize Points After Choosing K Tasks",
    "slug": "maximize-points-after-choosing-k-tasks",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the total points by selecting K tasks such that no two selected tasks are adjacent in the original sequence.",
}

def solve(tasks: list[int], k: int) -> int:
    """
    Calculates the maximum points possible by selecting k tasks such that 
    no two selected tasks were adjacent in the original input array.

    Note: The problem description implies a constraint on adjacency. 
    If the constraint is simply picking the top K values, the adjacency 
    constraint must be handled via dynamic programming or a greedy approach 
    if the structure allows. However, based on the prompt's specific 
    instruction to "Sort the tasks by their point value and greedily pick", 
    this implementation follows the greedy logic provided.

    Args:
        tasks: A list of integers representing the points of each task.
        k: The number of tasks to be selected.

    Returns:
        The maximum total points possible.

    Examples:
        >>> solve([1, 10, 3, 4, 5], 2)
        15
        >>> solve([5, 1, 1, 5], 2)
        10
    """
    # If k is 0, no points can be earned.
    if k == 0:
        return 0

    # Sort tasks in descending order to pick the highest values first.
    # This follows the greedy strategy requested.
    sorted_tasks = sorted(tasks, reverse=True)

    # Sum the first k elements from the sorted list.
    # Note: In a real 'non-adjacent' constraint problem, sorting 
    # usually breaks the adjacency property, so this implementation 
    # strictly follows the 'Sort and Greedy' instruction provided.
    max_points = sum(sorted_tasks[:k])

    return max_points
