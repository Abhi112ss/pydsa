METADATA = {
    "id": 800,
    "name": "Similar RGB Color",
    "slug": "similar_rgb_color",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the similar RGB color where each component is the nearest multiple of 17.",
}


def solve(color: str) -> str:
    """Convert a hex color string to its similar RGB color.

    Args:
        color: A string representing a hex color in the format "#RRGGBB",
            where each pair of characters is a hexadecimal number (0‑255).

    Returns:
        A string in the same format where each component (RR, GG, BB) is
        replaced by the nearest multiple of 17 (0x11). If a component is
        exactly halfway between two multiples, the larger multiple is chosen.

    Examples:
        >>> solve("#09f166")
        '#00ff66'
        >>> solve("#123456")
        '#111455'
    """
    # Extract the three two‑character components.
    components = [color[1:3], color[3:5], color[5:7]]

    similar_parts = []
    for hex_pair in components:
        original_value = int(hex_pair, 16)                     # decimal value 0‑255
        lower_multiple = (original_value // 17) * 17          # nearest lower multiple of 17
        upper_multiple = lower_multiple + 17 if lower_multiple < 255 else lower_multiple

        # Choose the multiple with smaller absolute difference; on tie pick the higher.
        if (original_value - lower_multiple) < (upper_multiple - original_value):
            chosen_value = lower_multiple
        else:
            chosen_value = upper_multiple

        similar_parts.append(f"{chosen_value:02x}")            # format as two‑digit hex

    return "#" + "".join(similar_parts)