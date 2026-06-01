METADATA = {
    "id": 2628,
    "name": "JSON Deep Equal",
    "slug": "json_deep_equal",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["recursion", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Determine if two JSON strings represent the same data structure by parsing and comparing their values.",
}

from typing import Any, Union, Dict, List


def solve(json1: str, json2: str) -> bool:
    """
    Determines if two JSON strings are deeply equal.

    Args:
        json1: The first JSON string.
        json2: The second JSON string.

    Returns:
        True if the JSON structures are deeply equal, False otherwise.

    Examples:
        >>> solve('{"a": [1, 2], "b": 3}', '{"a": [1, 2], "b": 3}')
        True
        >>> solve('{"a": 1}', '{"a": "1"}')
        False
    """

    def parse_json(s: str, index: int) -> tuple[Any, int]:
        """
        A recursive descent parser to convert a JSON string into Python objects.

        Args:
            s: The full JSON string.
            index: The current position in the string.

        Returns:
            A tuple containing the parsed object and the next index to process.
        """
        # Skip whitespace
        while index < len(s) and s[index].isspace():
            index += 1

        if index >= len(s):
            raise ValueError("Unexpected end of string")

        char = s[index]

        # Handle Objects (Dictionaries)
        if char == "{":
            return parse_object(s, index)

        # Handle Arrays (Lists)
        elif char == "[":
            return parse_array(s, index)

        # Handle Strings
        elif char == '"':
            return parse_string(s, index)

        # Handle Booleans, Null, and Numbers
        else:
            return parse_primitive(s, index)

    def parse_object(s: str, index: int) -> tuple[dict, int]:
        obj = {}
        index += 1  # Skip '{'
        
        while index < len(s):
            while index < len(s) and s[index].isspace():
                index += 1
            
            if index < len(s) and s[index] == "}":
                return obj, index + 1
            
            # Parse Key
            key, index = parse_string(s, index)
            
            # Skip whitespace and find colon
            while index < len(s) and s[index].isspace():
                index += 1
            if s[index] != ":":
                raise ValueError("Expected ':'")
            index += 1
            
            # Parse Value
            value, index = parse_json(s, index)
            obj[key] = value
            
            # Skip whitespace and find comma or end
            while index < len(s) and s[index].isspace():
                index += 1
            if index < len(s) and s[index] == ",":
                index += 1
            elif index < len(s) and s[index] == "}":
                continue
            else:
                raise ValueError("Expected ',' or '}'")
        
        return obj, index

    def parse_array(s: str, index: int) -> tuple[list, int]:
        arr = []
        index += 1  # Skip '['
        
        while index < len(s):
            while index < len(s) and s[index].isspace():
                index += 1
            
            if index < len(s) and s[index] == "]":
                return arr, index + 1
            
            value, index = parse_json(s, index)
            arr.append(value)
            
            while index < len(s) and s[index].isspace():
                index += 1
            if index < len(s) and s[index] == ",":
                index += 1
            elif index < len(s) and s[index] == "]":
                continue
            else:
                raise ValueError("Expected ',' or ']'")
        
        return arr, index

    def parse_string(s: str, index: int) -> tuple[str, int]:
        index += 1  # Skip opening quote
        start = index
        while index < len(s) and s[index] != '"':
            # Note: This implementation assumes no escaped quotes for simplicity, 
            # as per standard LeetCode JSON constraints unless specified.
            index += 1
        content = s[start:index]
        return content, index + 1

    def parse_primitive(s: str, index: int) -> tuple[Union[bool, float, int, None], int]:
        start = index
        # Allowed characters in primitives: numbers, booleans, null
        allowed = "0123456789.-truefalsenull"
        while index < len(s) and s[index] in allowed:
            index += 1
        
        token = s[start:index]
        
        if token == "true":
            return True, index
        if token == "false":
            return False, index
        if token == "null":
            return None, index
        
        # Try parsing as number
        try:
            if "." in token:
                return float(token), index
            return int(token), index
        except ValueError:
            raise ValueError(f"Invalid primitive: {token}")

    # 1. Parse both JSON strings into Python native objects
    # 2. Use Python's built-in equality operator which handles deep comparison for dicts/lists
    try:
        obj1, _ = parse_json(json1, 0)
        obj2, _ = parse_json(json2, 0)
        return obj1 == obj2
    except Exception:
        return False
