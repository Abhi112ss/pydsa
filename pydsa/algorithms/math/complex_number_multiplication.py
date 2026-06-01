METADATA = {
    "id": 537,
    "name": "Complex Number Multiplication",
    "slug": "complex-number-multiplication",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Multiply two complex numbers represented as strings in the format 'a+bi'.",
}

def solve(num1: str, num2: str) -> str:
    """
    Multiplies two complex numbers represented as strings.

    The formula for multiplication is:
    (a + bi) * (c + di) = (ac - bd) + (ad + bc)i

    Args:
        num1: A string representing the first complex number in 'a+bi' format.
        num2: A string representing the second complex number in 'a+bi' format.

    Returns:
        A string representing the product in 'a+bi' format.

    Examples:
        >>> solve("1+1i", "1+1i")
        '0+2i'
        >>> solve("1+i", "1-1i")
        '2+0i'
    """
    # Parse the first complex number
    # Split by '+' to separate real and imaginary parts, then strip the 'i'
    real1_str, imag1_str = num1.split('+')
    real1 = int(real1_str)
    imag1 = int(imag1_str[:-1])

    # Parse the second complex number
    real2_str, imag2_str = num2.split('+')
    real2 = int(real2_str)
    imag2 = int(imag2_str[:-1])

    # Apply the complex multiplication formula:
    # (a + bi)(c + di) = ac + adi + bci + bdi^2
    # Since i^2 = -1, this becomes (ac - bd) + (ad + bc)i
    res_real = (real1 * real2) - (imag1 * imag2)
    res_imag = (real1 * imag2) + (imag1 * real2)

    # Return formatted string
    return f"{res_real}+{res_imag}i"
