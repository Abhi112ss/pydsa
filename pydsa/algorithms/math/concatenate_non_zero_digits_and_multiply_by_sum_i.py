METADATA = {
    "id": 3754,
    "name": "Concatenate Non-Zero Digits and Multiply by Sum I",
    "slug": "concatenate_non_zero_digits_and_multiply_by_sum_i",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "brute_force"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(1)",
    "description": "Concatenate non-zero digits of numbers in an array and multiply the resulting number by the sum of the original numbers.",
}

def solve(nums: list[int]) -> int:
    """
    Concatenates all non-zero digits from the numbers in the list into a single 
    integer and multiplies it by the sum of the original numbers.

    Args:
        nums: A list of integers.

    Returns:
        The product of the concatenated non-zero digits and the sum of the input list.

    Examples:
        >>> solve([10, 2, 0])
        # Non-zero digits: 1, 2 -> Concatenated: 12. Sum: 10+2+0 = 12. 12 * 12 = 144.
        >>> solve([1, 2, 3])
        # Non-zero digits: 1, 2, 3 -> Concatenated: 123. Sum: 6. 123 * 6 = 738.
    """
    concatenated_str = ""
    total_sum = 0

    for num in nums:
        total_sum += num
        
        # Convert number to string to iterate through digits easily
        # or use mathematical approach to extract digits
        temp_num = abs(num)
        if temp_num == 0:
            continue
            
        # Extract digits in reverse order using modulo to avoid string overhead
        # but for concatenation, building a string is more intuitive for "order"
        # The problem implies digits are processed in the order they appear in the number
        s_num = str(temp_num)
        for digit in s_num:
            if digit != '0':
                concatenated_str += digit

    # If no non-zero digits were found, the concatenated value is 0
    concatenated_val = int(concatenated_str) if concatenated_str else 0
    
    return concatenated_val * total_sum
