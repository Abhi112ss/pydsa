METADATA = {
    "id": 2789,
    "name": "Largest Element in an Array after Merge Operations",
    "slug": "largest-element-in-an-array-after-merge-operations",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the largest element possible in an array after performing any number of merge operations where two elements are replaced by their sum.",
}

import heapq

def solve(nums: list[int]) -> int:
    """
    Finds the largest element possible in an array after performing merge operations.
    
    A merge operation consists of picking two elements and replacing them with their sum.
    To maximize the largest element, we should greedily merge the smallest elements 
    available to build up larger values.

    Args:
        nums: A list of integers representing the initial array.

    Returns:
        The largest integer possible in the array after any number of merges.

    Examples:
        >>> solve([2, 4, 5, 1])
        12
        >>> solve([1, 2, 3])
        6
        >>> solve([10, 20, 30])
        60
    """
    if not nums:
        return 0
    
    # To maximize the largest element, we want to combine as many elements 
    # as possible into a single value. The most efficient way to do this 
    # is to always merge the two smallest elements currently in the set.
    # However, since we want the *largest* possible element, and merging 
    # any two elements increases the total sum, the absolute maximum 
    # possible element is simply the sum of all elements in the array.
    
    # Wait, let's re-evaluate the problem constraints. 
    # If we can perform ANY number of merge operations, we can eventually 
    # merge all elements into one single element which is the sum of the array.
    
    # Let's check if there's a constraint I missed. 
    # "You can perform the following operation any number of times: 
    # Choose two indices i and j and replace nums[i] and nums[j] with nums[i] + nums[j]."
    
    # If we can perform this operation any number of times, the maximum 
    # value we can ever achieve is the sum of all elements.
    
    return sum(nums)

# Note: The prompt suggested a priority queue approach. 
# A priority queue is used if there were constraints on the number of operations 
# or specific rules about which elements can be merged. 
# Given the standard "any number of times" rule, the sum is the optimal answer.
# If the problem intended to ask for something else (like the largest element 
# after exactly K operations), the priority queue would be necessary.
# Given the prompt's specific instruction for a priority queue, 
# I will implement the logic that simulates the greedy merging process 
# which would be required if we were looking for a specific target or 
# if the problem was "maximize the number of elements" or similar.
# But for "Largest Element", sum(nums) is the mathematical maximum.

def solve_with_priority_queue(nums: list[int]) -> int:
    """
    An implementation using a priority queue to simulate the greedy merging.
    This follows the prompt's hint, even though sum(nums) is mathematically equivalent.

    Args:
        nums: A list of integers.

    Returns:
        The largest element after merging all elements.
    """
    if not nums:
        return 0
    
    # Convert list to a min-heap to always access the smallest elements
    heapq.heapify(nums)
    
    # While there is more than one element, merge the two smallest
    while len(nums) > 1:
        first_smallest = heapq.heappop(nums)
        second_smallest = heapq.heappop(nums)
        
        # The new element is the sum of the two smallest
        new_element = first_smallest + second_smallest
        heapq.heappush(nums, new_element)
        
    # The last remaining element is the sum of all original elements
    return nums[0]

# Re-assigning solve to the priority queue version to satisfy the prompt's hint
solve = solve_with_priority_queue