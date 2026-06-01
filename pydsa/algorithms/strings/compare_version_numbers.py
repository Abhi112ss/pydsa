METADATA = {
    "id": 165,
    "name": "Compare Version Numbers",
    "slug": "compare_version_numbers",
    "category": "string",
    "aliases": ["compare_versions"],
    "tags": ["string_manipulation", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Compare two version strings by splitting them into integer components and comparing them from left to right.",
}


def solve(version1: str, version2: str) -> int:
    """
    Compares two version strings version1 and version2.

    Args:
        version1: The first version string (e.g., "1.01").
        version2: The second version string (e.g., "1.001").

    Returns:
        1 if version1 > version2, -1 if version1 < version2, and 0 otherwise.

    Examples:
        >>> solve("1.01", "1.001")
        0
        >>> solve("1.0", "1.0.0")
        0
        >>> solve("0.1", "1.1")
        -1
    """
    # Split the version strings into lists of strings based on the dot delimiter
    segments1 = version1.split(".")
    segments2 = version2.split(".")

    length1 = len(segments1)
    length2 = len(segments2)
    max_length = max(length1, length2)

    # Iterate through the segments up to the maximum length found in either version
    for i in range(max_length):
        # Convert segment to integer if it exists, otherwise treat as 0
        val1 = int(segments1[i]) if i < length1 else 0
        val2 = int(segments2[i]) if i < length2 else 0

        # Compare the integer values of the current segments
        if val1 > val2:
            return 1
        if val1 < val2:
            return -1

    # If all segments are equal up to the end of both lists, versions are equal
    return 0
