METADATA = {
    "id": 1108,
    "name": "Defanging an IP Address",
    "slug": "defanging_an_ip_address",
    "category": "string",
    "aliases": [],
    "tags": ["strings", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Replace each '.' in an IP address with '[.]'.",
}


def solve() -> None:
    """Read an IPv4 address from standard input, defang it, and print the result.

    Args:
        None (input is read from stdin).

    Returns:
        None (the defanged IP address is printed to stdout).

    Examples:
        >>> # Input: 1.1.1.1
        >>> # Output: 1[.]1[.]1[.]1
        >>> import sys, io
        >>> sys.stdin = io.StringIO('1.1.1.1\\n')
        >>> solve()
        1[.]1[.]1[.]1
    """
    import sys

    raw_input: str = sys.stdin.readline().strip()
    # Build the defanged address character by character.
    defanged_parts: list[str] = []
    for character in raw_input:
        if character == '.':
            defanged_parts.append('[.]')  # replace dot with the defanged token
        else:
            defanged_parts.append(character)
    defanged_address: str = ''.join(defanged_parts)
    sys.stdout.write(defanged_address)