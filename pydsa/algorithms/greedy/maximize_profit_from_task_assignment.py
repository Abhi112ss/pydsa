METADATA = {
    "id": 3476,
    "name": "Maximize Profit from Task Assignment",
    "slug": "maximize-profit-from-task-assignment",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the total profit by assigning tasks to workers using a greedy approach with two pointers.",
}

def solve(tasks: list[int], workers: list[int]) -> int:
    """
    Calculates the maximum profit by assigning tasks to workers.
    
    The strategy is to pair the highest-value tasks with the highest-value 
    workers to maximize the sum, provided the worker's strength is 
    greater than or equal to the task's requirement. Since the problem 
    implies we want to maximize profit and we can assign any task to any 
    worker (assuming worker >= task), sorting both allows us to use 
    a two-pointer approach.

    Args:
        tasks: A list of integers representing task requirements.
        workers: A list of integers representing worker strengths.

    Returns:
        The maximum total profit possible.

    Examples:
        >>> solve([1, 2, 3], [1, 2, 3])
        6
        >>> solve([5, 10], [5, 10])
        15
    """
    # Sort both lists to enable the greedy two-pointer strategy
    tasks.sort()
    workers.sort()
    
    n = len(tasks)
    total_profit = 0
    
    # Pointer for the smallest available task
    task_left = 0
    # Pointer for the largest available task
    task_right = n - 1
    # Pointer for the smallest available worker
    worker_left = 0
    # Pointer for the largest available worker
    worker_right = n - 1
    
    # We need to pair n tasks with n workers.
    # To maximize profit, we try to match the largest tasks with the largest workers.
    # However, if the largest worker cannot handle the largest task, 
    # that task is impossible to complete with the current set of workers.
    # Wait, the standard version of this problem (like LeetCode 826/2035) 
    # usually asks for max profit given constraints. 
    # Given the prompt's specific instruction: "pair the best available worker 
    # with the best task", we implement the greedy pairing.
    
    # Standard Greedy for this type of problem:
    # Sort both. Match largest worker with largest task if possible.
    # If largest worker can't do largest task, largest worker is "wasted" 
    # on the largest possible task they CAN do, or we match smallest tasks 
    # to smallest workers to save big workers for big tasks.
    
    # Based on the prompt's specific logic: "Sort both... use two-pointer 
    # approach to pair the best available worker with the best task."
    
    # We iterate through workers from largest to smallest
    # and try to assign the largest possible task they can handle.
    
    # Re-evaluating based on "Maximize Profit":
    # If we want to maximize the sum of tasks assigned:
    # We should pair the largest workers with the largest tasks they can satisfy.
    
    # Let's use the two-pointer approach:
    # Sort tasks and workers.
    # For each worker (from largest to smallest), try to pick the largest task.
    
    # Actually, the most efficient way to maximize sum is to pair 
    # the largest workers with the largest tasks they can actually perform.
    
    # Correct Greedy:
    # Sort tasks ascending, workers ascending.
    # Use two pointers for tasks (left, right) and workers (left, right).
    # To maximize profit, we want to use our best workers for the best tasks.
    
    # If the largest worker can do the largest task, do it.
    # If not, the largest task cannot be completed by anyone (if workers are sorted),
    # so we skip that task (or in some variations, the worker is used elsewhere).
    # But in a standard "assign all" scenario, we match.
    
    # Let's implement the logic: Match largest worker with largest task.
    # If worker >= task: profit += task, move both pointers.
    # If worker < task: task is too big for this worker, move task pointer down.
    
    # Wait, if worker < task, the task is too big for the CURRENT largest worker.
    # Since workers are sorted, this task is too big for ALL remaining workers.
    # So we must skip this task.
    
    task_idx = n - 1
    worker_idx = n - 1
    
    while task_idx >= 0 and worker_idx >= 0:
        if workers[worker_idx] >= tasks[task_idx]:
            # Best worker can take the best task
            total_profit += tasks[task_idx]
            task_idx -= 1
            worker_idx -= 1
        else:
            # Best task is too hard for the best worker
            # Skip this task to try a smaller one
            task_idx -= 1
            
    return total_profit
