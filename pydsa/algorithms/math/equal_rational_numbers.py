METADATA = {
    "id": 972,
    "name": "Equal Rational Numbers",
    "slug": "equal-rational-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["string", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if two strings representing repeating decimals represent the same rational number.",
}

def solve(a: str, b: str) -> bool:
    """
    Args:
        a: A string representing a rational number in decimal form.
        b: A string representing a rational number in decimal form.

    Returns:
        True if the two rational numbers are equal, False otherwise.
    """
    def parse_decimal(decimal_str: str) -> tuple[int, int]:
        if "." not in decimal_str:
            return int(decimal_str), 1
        
        integer_part_str, fractional_part_str = decimal_str.split(".")
        integer_part = int(integer_part_str)
        
        if "(" not in fractional_part_str:
            denominator = 10 ** len(fractional_part_str)
            numerator = int(fractional_part_str) if fractional_part_str else 0
            return integer_part * denominator + numerator, denominator
        
        non_repeating_part, repeating_part = fractional_part_str.split("(")
        repeating_part = repeating_part.rstrip(")")
        
        non_repeating_len = len(non_repeating_part)
        repeating_len = len(repeating_part)
        
        non_repeating_val = int(non_repeating_part) if non_repeating_part else 0
        repeating_val = int(repeating_part)
        
        denominator = (10 ** repeating_len - 1) * (10 ** non_repeating_len)
        
        numerator = (non_repeating_val * (10 ** repeating_len - 1) + repeating_val) * (10 ** non_repeating_len)
        
        total_numerator = integer_part * denominator + numerator
        return total_numerator, denominator

    def gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x

    num_a, den_a = parse_decimal(a)
    num_b, den_b = parse_decimal(b)
    
    common_den = den_a * den_b
    return num_a * den_b == num_b * den_a