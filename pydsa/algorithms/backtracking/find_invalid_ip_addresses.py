METADATA = {
    "id": 3451,
    "name": "Find Invalid IP Addresses",
    "slug": "find_invalid_ip_addresses",
    "category": "String",
    "aliases": [],
    "tags": ["backtracking", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find all possible combinations of four segments that form an invalid IPv4 address from a given string of digits.",
}

def solve(s: str) -> list[str]:
    """
    Args:
        s: A string consisting of digits.

    Returns:
        A list of all invalid IPv4 address strings that can be formed from the input.
    """
    all_combinations = []
    n = len(s)

    def is_valid_segment(segment: str) -> bool:
        if not segment:
            return False
        if len(segment) > 3:
            return False
        if len(segment) > 1 and segment[0] == '0':
            return False
        return True

    def backtrack(start_index: int, current_segments: list[str]):
        if len(current_segments) == 4:
            if start_index == n:
                all_combinations.append(".".join(current_segments))
            return

        for length in range(1, 4):
            if start_index + length <= n:
                segment = s[start_index : start_index + length]
                current_segments.append(segment)
                backtrack(start_index + length, current_segments)
                current_segments.pop()

    backtrack(0, [])

    valid_ips = set()
    for ip in all_combinations:
        segments = ip.split(".")
        if len(segments) == 4:
            is_valid = True
            for seg in segments:
                if not is_valid_segment(seg):
                    is_valid = False
                    break
            if is_valid:
                valid_ips.add(ip)

    invalid_ips = []
    for ip in all_combinations:
        if ip not in valid_ips:
            invalid_ips.append(ip)

    return invalid_ips