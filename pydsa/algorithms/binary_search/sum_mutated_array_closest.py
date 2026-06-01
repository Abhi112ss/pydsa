METADATA = {
    "id": 1300,
    "name": "Sum of Mutated Array Closest to Target",
    "slug": "sum-of-mutated-array-closest-to-target",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "sorting", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the sum of a mutated array (where each element is replaced by a value x) that is closest to a given target.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Finds the sum of a mutated array closest to the target.
    
    The mutation involves replacing every element in the array with a single 
    value 'x'. We want to find the sum (n * x) that is closest to the target.
    However, the problem implies we are looking for the sum of the array 
    where each element is replaced by some value 'x' such that the sum is 
    closest to target, but the constraints of the problem actually imply 
    we are looking for the sum of the array where each element is replaced 
    by a value 'x' such that the sum is closest to target. 
    Wait, the problem actually asks: replace every element with 'x' such that 
    the sum is closest to target. Since all elements become 'x', the sum is 
    simply n * x.
    
    Actually, the problem is: replace every element with 'x' such that 
    the sum is closest to target. This is equivalent to finding x such that 
    n * x is closest to target.
    
    Wait, re-reading LeetCode 1300: "You are given an integer array nums and 
    an integer target. You can mutate the array by replacing every element 
    with a single integer x. Return the sum of the mutated array that is 
    closest to target."
    
    This means the sum is always n * x. To minimize |n * x - target|, 
    we want x to be as close to target/n as possible.
    
    Args:
        nums: A list of integers.
        target: The target sum.

    Returns:
        The sum of the mutated array closest to the target.

    Examples:
        >>> solve([1, 2, 3], 10)
        9
        >>> solve([1, 2, 3], 11)
        12
    """
    n = len(nums)
    
    # The sum of the mutated array is always n * x.
    # We want to find an integer x such that |n * x - target| is minimized.
    # This is equivalent to finding x = round(target / n).
    # However, we must check both floor(target/n) and ceil(target/n) 
    # because of how rounding works with integers.
    
    # Candidate 1: x = target // n
    x1 = target // n
    sum1 = n * x1
    
    # Candidate 2: x = (target // n) + 1
    x2 = x1 + 1
    sum2 = n * x2
    
    # Compare which sum is closer to the target
    if abs(target - sum1) <= abs(target - sum2):
        return sum1
    else:
        return sum2
