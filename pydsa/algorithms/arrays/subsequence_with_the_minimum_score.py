METADATA = {
    "id": 2565,
    "name": "Subsequence With the Minimum Score",
    "slug": "subsequence-with-the-minimum-score",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum score of a non-empty subsequence where the score is the minimum element multiplied by the sum of the remaining elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum score of a subsequence.
    
    The score is defined as: min(subsequence) * (sum(subsequence) - min(subsequence)).
    To minimize this, we iterate through each element treating it as the minimum.
    If nums[i] is the minimum, we want the sum of the rest of the elements to be 
    as small as possible. However, the problem implies we can pick any subsequence.
    Actually, for a fixed minimum element at index i, to minimize the score, 
    we should pick the smallest possible sum of the remaining elements. 
    Wait, the problem asks for the minimum score among ALL possible subsequences.
    If we pick nums[i] as the minimum, the score is nums[i] * (sum of other elements).
    To minimize this, we should pick the smallest possible 'other elements'.
    But the elements must be part of a subsequence where nums[i] is the minimum.
    This means all other elements in the subsequence must be >= nums[i].
    To minimize the sum, we should pick only ONE other element that is >= nums[i]
    and is the smallest such element.
    
    Actually, the problem is simpler: for a fixed minimum element nums[i], 
    the score is nums[i] * (sum of some elements all >= nums[i]).
    To minimize this, we should pick the smallest possible sum of elements 
    that are all >= nums[i]. The smallest such sum is just the smallest 
    element in the array that is >= nums[i] (excluding nums[i] itself).
    
    Wait, the problem states: "the sum of the elements in the subsequence excluding the minimum element".
    If we pick a subsequence of size 2, say {min, x}, the score is min * x.
    If we pick a subsequence of size 3, say {min, x, y}, the score is min * (x + y).
    Since all elements are positive, min * x is always <= min * (x + y).
    Therefore, the optimal subsequence will always have exactly 2 elements.
    The problem reduces to finding min(nums[i] * nums[j]) where nums[i] <= nums[j] 
    and i != j.
    
    Wait, let's re-read. "Subsequence" means we pick elements. 
    If we pick nums[i] as the minimum, we want to pick other elements such that 
    they are all >= nums[i] and their sum is minimized.
    The smallest possible sum of "other elements" is simply the smallest 
    element in the array that is >= nums[i] (and not the same instance).
    
    Actually, the constraint is that we can pick ANY subsequence. 
    If we pick a subsequence of size 2, the score is nums[i] * nums[j].
    To minimize this, we just need to find the two smallest elements in the array.
    Let the two smallest elements be a and b (a <= b).
    The score is a * b.
    
    Let's check the constraints and examples.
    Example 1: nums = [4,3,5], min score is 3 * 4 = 12.
    Example 2: nums = [1,1,2,2,3], min score is 1 * 1 = 1.
    
    Wait, if the array is [1, 1, 2, 2, 3], the two smallest are 1 and 1. 1 * 1 = 1.
    If the array is [4, 3, 5], the two smallest are 3 and 4. 3 * 4 = 12.
    
    The logic is: The minimum score is always achieved by a subsequence of size 2 
    consisting of the two smallest elements in the array.
    
    Args:
        nums: A list of positive integers.

    Returns:
        The minimum score as an integer.

    Examples:
        >>> solve([4, 3, 5])
        12
        >>> solve([1, 1, 2, 2, 3])
        1
    """
    # To minimize min(sub) * (sum(sub) - min(sub)), we should minimize the sum.
    # Since all elements are positive, the smallest sum is achieved by 
    # picking the smallest possible second element.
    # Thus, we only need the two smallest elements from the array.
    
    if len(nums) < 2:
        return 0
    
    # Find the two smallest elements in O(n) time
    first_min = float('inf')
    second_min = float('inf')
    
    for num in nums:
        if num < first_min:
            # Current number is smaller than the smallest found so far
            second_min = first_min
            first_min = num
        elif num < second_min:
            # Current number is between first_min and second_min
            second_min = num
            
    return int(first_min * second_min)
