METADATA = {
    "id": 2457,
    "name": "Minimum Addition to Make Integer Beautiful",
    "slug": "minimum-addition-to-make-integer-beautiful",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum non-negative integer to add to n such that all digits of the resulting integer are non-zero.",
}

def solve(n: int, digits: list[int]) -> int:
    """
    Args:
        n: The initial integer.
        digits: A list of digits that are considered 'bad' (zero).

    Returns:
        The minimum non-negative integer to add to n to make all its digits non-zero.
    """
    bad_digits_set = set(digits)
    current_n = n
    power_of_ten = 1
    additions = 0

    while True:
        current_digit = (current_n // power_of_ten) % 10
        
        if current_digit in bad_digits_set:
            remainder_to_add = power_of_ten - (current_n % power_of_ten)
            additions += remainder_to_add
            current_n += remainder_to_add
        
        power_of_ten *= 10
        
        if current_n < power_of_ten:
            all_digits_valid = True
            temp_n = current_n
            while temp_n > 0:
                if (temp_n % 10) in bad_digits_set:
                    all_digits_valid = False
                    break
                temp_n //= 10
            
            if all_digits_valid:
                return additions
        
        if power_of_ten > current_n * 10:
            return additions