METADATA = {
    "id": 907,
    "name": "Sum of Subarray Minimums",
    "slug": "sum-of-subarray-minimums",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the sum of the minimum elements of all possible contiguous subarrays.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the sum of the minimum elements of all contiguous subarrays.

    The algorithm uses a monotonic stack to find the distance to the nearest 
    smaller element to the left and the nearest smaller element to the right 
    for every element in the array. The contribution of arr[i] to the total sum 
    is arr[i] * (distance_to_left) * (distance_to_right).

    Args:
        arr: A list of integers.

    Returns:
        The sum of minimums of all subarrays modulo 10^9 + 7.

    Examples:
        >>> solve([3, 1, 2, 4])
        8
        >>> solve([1, 2, 3])
        6
    """
    MOD = 10**9 + 7
    n = len(arr)
    
    # left_distances[i] stores the number of elements to the left of i 
    # (including i) that are greater than arr[i] before hitting a smaller element.
    left_distances = [0] * n
    # right_distances[i] stores the number of elements to the right of i 
    # (including i) that are greater than or equal to arr[i] before hitting a smaller element.
    # Note: We use strictly greater on one side and greater-or-equal on the other 
    # to handle duplicate elements correctly and avoid double-counting subarrays.
    right_distances = [0] * n
    
    # Monotonic stack to find the nearest smaller element to the left
    stack: list[int] = []
    for i in range(n):
        # Pop elements that are greater than the current element
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        
        # If stack is empty, all elements to the left are >= arr[i]
        if not stack:
            left_distances[i] = i + 1
        else:
            # Distance is the gap between current index and the index of the smaller element
            left_distances[i] = i - stack[-1]
        stack.append(i)
        
    # Clear stack for the next pass
    stack.clear()
    
    # Monotonic stack to find the nearest smaller element to the right
    for i in range(n - 1, -1, -1):
        # Use >= here to handle duplicates: one side is strictly smaller, one is smaller-or-equal
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
            
        if not stack:
            right_distances[i] = n - i
        else:
            right_distances[i] = stack[-1] - i
        stack.append(i)
        
    # Calculate total sum using the contribution of each element
    total_sum = 0
    for i in range(n):
        # Contribution = value * (ways to pick left boundary) * (ways to pick right boundary)
        contribution = arr[i] * left_distances[i] * right_distances[i]
        total_sum = (total_sum + contribution) % MOD
        
    return total_sum
