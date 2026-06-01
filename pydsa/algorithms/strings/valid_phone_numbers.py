METADATA = {
    "id": 193,
    "name": "Valid Phone Numbers",
    "slug": "valid_phone_numbers",
    "category": "Shell",
    "aliases": [],
    "tags": ["shell", "regex"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all phone numbers that match the two valid formats: (xxx) xxx-xxxx or xxx-xxx-xxxx.",
}

def solve(file_path: str) -> list[str]:
    """
    Reads a file containing phone numbers (one per line) and returns only those that match
    valid phone number formats: (xxx) xxx-xxxx or xxx-xxx-xxxx (where x is a digit).

    Args:
        file_path (str): Path to the text file containing phone numbers.

    Returns:
        list[str]: A list of valid phone numbers matching the allowed formats.

    Examples:
        >>> # Given file.txt contains:
        # 987-123-4567
        # (123) 456-7890
        # 555-555-5555
        # (111) 222-3333
        # abc-def-ghij
        >>> solve("file.txt")
        ['987-123-4567', '(123) 456-7890', '555-555-5555', '(111) 222-3333']
    """
    import re

    pattern = re.compile(r'^(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})$')
    valid_numbers = []

    with open(file_path, 'r') as file:
        for line in file:
            phone_number = line.strip()
            # Check if the phone number matches either of the two valid formats
            if pattern.match(phone_number):
                valid_numbers.append(phone_number)

    return valid_numbers