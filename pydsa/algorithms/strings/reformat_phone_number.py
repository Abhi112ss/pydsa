METADATA = {
    "id": 1694,
    "name": "Reformat Phone Number",
    "slug": "reformat_phone_number",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reformat a phone number string according to specific grouping rules."
}


def solve(number: str) -> str:
    """Reformat a phone number string according to the required grouping.

    Args:
        number: The original phone number containing digits, spaces, and dashes.

    Returns:
        A reformatted phone number where digits are grouped in blocks of three
        separated by dashes, except that the last block can be of size two or
        three. If the final block would be a single digit, the last two blocks
        are both of size two.

    Examples:
        >>> solve("1-23-45 6")
        '123-456'
        >>> solve("123 4-567")
        '123-45-67'
        >>> solve("123 4-5678")
        '123-456-78'
    """
    # Extract only digit characters.
    digit_list = [char for char in number if char.isdigit()]

    result_blocks: list[str] = []
    index = 0
    total_digits = len(digit_list)

    while total_digits - index > 0:
        remaining = total_digits - index
        if remaining > 4:
            # Take a block of three digits.
            block = ''.join(digit_list[index:index + 3])
            result_blocks.append(block)
            index += 3
        else:
            if remaining == 4:
                # Split the last four digits into two blocks of two.
                first_block = ''.join(digit_list[index:index + 2])
                second_block = ''.join(digit_list[index + 2:index + 4])
                result_blocks.extend([first_block, second_block])
            else:
                # Remaining is 2 or 3 digits; take them as the final block.
                block = ''.join(digit_list[index:])
                result_blocks.append(block)
            break

    # Join blocks with dashes.
    return '-'.join(result_blocks)