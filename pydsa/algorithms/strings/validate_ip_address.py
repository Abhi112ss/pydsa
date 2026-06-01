METADATA = {
    "id": 468,
    "name": "Validate IP Address",
    "slug": "validate-ip-address",
    "category": "String",
    "aliases": [],
    "tags": ["string", "regex"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given string is a valid IPv4 or IPv6 address.",
}

def solve(ip: str) -> str:
    """
    Validates whether the given string is a valid IPv4 or IPv6 address.

    Args:
        ip: The input string to validate.

    Returns:
        "IPv4" if valid IPv4, "IPv6" if valid IPv6, or "Neither" otherwise.

    Examples:
        >>> solve("172.16.254.1")
        'IPv4'
        >>> solve("2001:0db8:85a3:0:0:8A2E:0370:7334")
        'IPv6'
        >>> solve("256.256.256.256")
        'Neither'
        >>> solve("2001:db8:85a3::8A2E:0370:7334")
        'Neither'
    """
    if "." in ip:
        return _is_valid_ipv4(ip)
    elif ":" in ip:
        return _is_valid_ipv6(ip)
    return "Neither"


def _is_valid_ipv4(ip: str) -> str:
    """Checks if the string follows IPv4 format: four decimal segments [0-255]."""
    parts = ip.split(".")
    if len(parts) != 4:
        return "Neither"

    for part in parts:
        # Check if part is numeric and not empty
        if not part.isdigit():
            return "Neither"
        
        # Check for leading zeros: "0" is okay, but "01" is not
        if len(part) > 1 and part[0] == "0":
            return "Neither"
        
        # Check range [0, 255]
        val = int(part)
        if val < 0 or val > 255:
            return "Neither"

    return "IPv4"


def _is_valid_ipv6(ip: str) -> str:
    """Checks if the string follows IPv6 format: eight hex segments [0-ffff]."""
    parts = ip.split(":")
    if len(parts) != 8:
        return "Neither"

    hex_digits = "0123456789abcdefABCDEF"
    for part in parts:
        # Each segment must be 1-4 characters long
        if not (1 <= len(part) <= 4):
            return "Neither"
        
        # Check if all characters in segment are valid hex digits
        for char in part:
            if char not in hex_digits:
                return "Neither"

    return "IPv6"
