METADATA = {
    "id": 2495,
    "name": "Number of Subarrays Having Even Product",
    "slug": "number-of-subarrays-having-even-product",
    "category": "Math",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays where the product of all elements is even.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of subarrays whose product is even.
    
    A product of integers is even if and only if at least one integer in the 
    subarray is even. It is easier to calculate the total number of subarrays 
    and subtract the number of subarrays that contain only odd numbers.

    Args:
        nums: A list of integers.

    Returns:
        The total count of subarrays with an even product.

    Examples:
        >>> solve([2, 3, 4, 5])
        8
        >>> solve([1, 2, 3, 4, 5, 6])
        15
    """
    n = len(nums)
    # Total number of subarrays in an array of length n is n * (n + 1) // 2
    total_subarrays = n * (n + 1) // 2
    
    odd_subarrays_count = 0
    current_odd_streak = 0
    
    for num in nums:
        if num % 2 != 0:
            # If the number is odd, increment the current streak of odd numbers
            current_odd_streak += 1
        else:
            # If the number is even, the streak of odd numbers is broken.
            # Calculate how many subarrays were formed by the preceding odd streak.
            # A streak of length 'k' produces k * (k + 1) // 2 subarrays.
            odd_subarrays_count += (current_odd_streak * (current_odd_streak + 1)) // 2
            current_odd_streak = 0
            
    # Add the last streak of odd numbers if the array ended with an odd number
    odd_subarrays_count += (current_odd_streak * (current_odd_streak + 1)) // 2
    
    # Even product subarrays = Total subarrays - Subarrays with only odd numbers
    return total_subarrays - odd_subarrays_count
