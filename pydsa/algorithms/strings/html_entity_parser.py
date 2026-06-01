METADATA = {
    "id": 1410,
    "name": "HTML Entity Parser",
    "slug": "html-entity-parser",
    "category": "String",
    "aliases": [],
    "tags": ["string", "hash table"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Replace specific HTML entities in a string with their corresponding characters.",
}

def solve(s: str) -> str:
    """
    Parses a string and replaces specific HTML entities with their character equivalents.

    The entities to be replaced are:
    - "&amp;" -> "&"
    - "&lt;" -> "<"
    - "&gt;" -> ">"

    Args:
        s: The input string containing potential HTML entities.

    Returns:
        A string where all recognized HTML entities have been replaced.

    Examples:
        >>> solve("Hello &amp; welcome!")
        'Hello & welcome!'
        >>> solve("a &lt; b &amp; c &gt; d")
        'a < b & c > d'
        >>> solve("no entities here")
        'no entities here'
    """
    # Mapping of HTML entities to their character representations
    entity_map = {
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">"
    }
    
    # Pre-calculate lengths to avoid repeated len() calls in the loop
    # and to handle the lookahead logic efficiently.
    result_chars = []
    n = len(s)
    i = 0
    
    while i < n:
        # Check if we have encountered the start of a potential entity
        if s[i] == "&":
            found_entity = False
            # Try to match the current substring starting at i with known entities
            for entity, char in entity_map.items():
                entity_len = len(entity)
                # Check if the substring from current index matches the entity
                if s.startswith(entity, i):
                    result_chars.append(char)
                    i += entity_len
                    found_entity = True
                    break
            
            # If no entity matched, treat the ampersand as a literal character
            if not found_entity:
                result_chars.append(s[i])
                i += 1
        else:
            # Regular character, append and move to next
            result_chars.append(s[i])
            i += 1
            
    return "".join(result_chars)
