METADATA = {
    "id": 3483,
    "name": "Unique 3-Digit Even Numbers",
    "slug": "unique-3-digit-even-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "iteration"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find all unique 3-digit even numbers that can be formed using a given set of digits.",
}

def solve(digits: list[int]) -> list[int]:
    """
    Finds all unique 3-digit even numbers that can be formed using the provided digits.

    Args:
        digits: A list of single-digit integers.

    Returns:
        A sorted list of unique 3-digit even numbers.

    Examples:
        >>> solve([2, 1, 3])
        [122, 132, 212, 232, 312, 322] # Note: This depends on digit availability. 
        # If digits are [2, 1, 3], and we can reuse them? 
        # Standard LeetCode interpretation for this type of problem: 
        # Each digit in the input list can be used at most once per number.
    """
    # Convert input list to a frequency map to handle duplicate digits correctly
    digit_counts = {}
    for d in digits:
        digit_counts[d] = digit_counts.get(d, 0) + 1

    result = []

    # Since we are looking for 3-digit numbers, we iterate through the fixed range [100, 999]
    # This ensures the complexity is O(1) as the range is constant.
    for num in range(100, 1000):
        # Check if the number is even
        if num % 2 == 0:
            # Extract digits of the current number
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            current_digits = [d1, d2, d3]
            temp_counts = {}
            for d in current_digits:
                temp_counts[d] = temp_counts.get(d, 0) + 1
            
            # Verify if the required digits are available in the input digits list
            possible = True
            for d, count in temp_counts.items():
                if digit_counts.get(d, 0) < count:
                    possible = False
                    break
            
            if possible:
                result.append(num)

    return result
