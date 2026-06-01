METADATA = {
    "id": 2342,
    "name": "Max Sum of a Pair With Equal Sum of Digits",
    "slug": "max-sum-of-a-pair-with-equal-sum-of-digits",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of two numbers in an array that have the same sum of digits.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of two numbers in the list that have the same sum of digits.

    Args:
        nums: A list of positive integers.

    Returns:
        The maximum sum of a pair with equal digit sums, or -1 if no such pair exists.

    Examples:
        >>> solve([12, 15, 18, 9])
        27
        >>> solve([1, 2, 3, 4, 5])
        -1
    """
    # Maps digit_sum -> largest_number_seen_with_that_sum
    digit_sum_to_max_val: dict[int, int] = {}
    max_pair_sum: int = -1

    for num in nums:
        # Calculate the sum of digits for the current number
        current_digit_sum = 0
        temp_num = num
        while temp_num > 0:
            current_digit_sum += temp_num % 10
            temp_num //= 10

        # If we have seen this digit sum before, we can form a pair
        if current_digit_sum in digit_sum_to_max_val:
            # Update the global maximum sum if the current pair is larger
            current_pair_sum = num + digit_sum_to_max_val[current_digit_sum]
            if current_pair_sum > max_pair_sum:
                max_pair_sum = current_pair_sum
            
            # Keep the largest number for this digit sum to maximize future pairs
            if num > digit_sum_to_max_val[current_digit_sum]:
                digit_sum_to_max_val[current_digit_sum] = num
        else:
            # First time seeing this digit sum, store the number
            digit_sum_to_max_val[current_digit_sum] = num

    return max_pair_sum
