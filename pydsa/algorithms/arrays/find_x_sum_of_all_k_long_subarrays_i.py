METADATA = {
    "id": 3318,
    "name": "Find X-Sum of All K-Long Subarrays I",
    "slug": "find_x_sum_of_all_k_long_subarrays_i",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of bitwise X-sums for all subarrays of length k, where X-sum is defined by bitwise operations.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the sum of X-sums for all subarrays of length k.
    The X-sum of a subarray is defined as the bitwise XOR of all elements 
    in the subarray, but specifically for this problem context (based on 
    standard X-sum definitions in competitive programming), it refers to 
    the bitwise XOR sum.

    Args:
        nums: A list of integers.
        k: The length of the subarrays to consider.

    Returns:
        The sum of the XOR sums of all subarrays of length k.

    Examples:
        >>> solve([1, 2, 3, 4], 2)
        # Subarrays: [1,2] -> 1^2=3; [2,3] -> 2^3=1; [3,4] -> 3^4=7. Sum = 3+1+7 = 11.
        11
    """
    MOD = 10**9 + 7
    n = len(nums)
    current_xor_sum = 0
    total_x_sum = 0

    # Initialize the XOR sum for the first window of size k
    for i in range(k):
        current_xor_sum ^= nums[i]
    
    total_x_sum = current_xor_sum

    # Slide the window across the array
    for i in range(k, n):
        # Remove the element that is sliding out of the window (i - k)
        # and add the element that is sliding into the window (i)
        # XORing the same value twice cancels it out
        current_xor_sum ^= nums[i - k]
        current_xor_sum ^= nums[i]
        
        total_x_sum = (total_x_sum + current_xor_sum) % MOD

    return total_x_sum
