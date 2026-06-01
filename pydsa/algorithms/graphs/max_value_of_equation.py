METADATA = {
    "id": 1499,
    "name": "Max Value of Equation",
    "slug": "max-value-of-equation",
    "category": "Hard",
    "aliases": [],
    "tags": ["math", "graph", "dijkstra"],
    "difficulty": "hard",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the maximum value of x[i] + x[j] + y[i] * y[j] given the constraint |y[i] - y[j]| <= k.",
}

import heapq

def solve(x: list[int], y: list[int], k: int) -> int:
    """
    Args:
        x: A list of integers representing the first part of the equation.
        y: A list of integers representing the second part of the equation.
        k: An integer representing the maximum allowed difference between y values.

    Returns:
        The maximum value of x[i] + x[j] + y[i] * y[j] for any i != j such that |y[i] - y[j]| <= k.
    """
    points = []
    for i in range(len(x)):
        points.append((y[i], x[i]))
    
    points.sort()
    
    max_value = -float('inf')
    max_heap = []
    left_pointer = 0
    
    for current_y, current_x in points:
        while left_pointer < len(points) and current_y - points[left_pointer][0] > k:
            pass
        
        while max_heap and current_y - max_heap[0][0] > k:
            heapq.heappop(max_heap)
            
        if max_heap:
            best_prev_y, best_prev_x = max_heap[0]
            max_value = max(max_value, current_x + best_prev_x + current_y * best_prev_y)
            
        heapq.heappush(max_heap, (-current_x, current_y))
        
    return int(max_value)

def solve(x: list[int], y: list[int], k: int) -> int:
    """
    Args:
        x: A list of integers representing the first part of the equation.
        y: A list of integers representing the second part of the equation.
        k: An integer representing the maximum allowed difference between y values.

    Returns:
        The maximum value of x[i] + x[j] + y[i] * y[j] for any i != j such that |y[i] - y[j]| <= k.
    """
    points = sorted(zip(y, x))
    max_val = -float('inf')
    heap = []
    left = 0
    
    for current_y, current_x in points:
        while heap and current_y - heap[0][1] > k:
            heapq.heappop(heap)
            
        if heap:
            best_neg_x, best_y = heap[0]
            max_val = max(max_val, current_x + (-best_neg_x) + current_y * best_y)
            
        heapq.heappush(heap, (-current_x, current_y))
        
    return int(max_val)

def solve(x: list[int], y: list[int], k: int) -> int:
    """
    Args:
        x: A list of integers representing the first part of the equation.
        y: A list of integers representing the second part of the equation.
        k: An integer representing the maximum allowed difference between y values.

    Returns:
        The maximum value of x[i] + x[j] + y[i] * y[j] for any i != j such that |y[i] - y[j]| <= k.
    """
    points = sorted(zip(y, x))
    max_val = -float('inf')
    max_heap = []
    
    for current_y, current_x in points:
        while max_heap and current_y - max_heap[0][1] > k:
            heapq.heappop(max_heap)
            
        if max_heap:
            neg_prev_x, prev_y = max_heap[0]
            max_val = max(max_val, current_x + (-neg_prev_x) + current_y * prev_y)
            
        heapq.heappush(max_heap, (-current_x, current_y))
        
    return int(max_val)