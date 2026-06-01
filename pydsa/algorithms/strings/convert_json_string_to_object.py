METADATA = {
    "id": 2759,
    "name": "Convert JSON String to Object",
    "slug": "convert_json_string_to_object",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "recursion", "parsing"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Implement a parser to convert a JSON-formatted string into its corresponding Python object representation.",
}

from typing import Any, Union


class JSONParser:
    """
    A recursive descent parser for a subset of JSON.
    Supports: Objects {}, Arrays [], Strings "", Numbers, Booleans, and Null.
    """

    def __init__(self, json_str: str):
        self.json_str = json_str
        self.index = 0
        self.length = len(json_str)

    def _skip_whitespace(self) -> None:
        """Advances the index past any whitespace characters."""
        while self.index < self.length and self.json_str[self.index].isspace():
            self.index += 1

    def _parse_value(self) -> Any:
        """Parses the next JSON value based on the current character."""
        self._skip_whitespace()
        if self.index >= self.length:
            raise ValueError("Unexpected end of input")

        char = self.json_str[self.index]

        if char == "{":
            return self._parse_object()
        elif char == "[":
            return self._parse_array()
        elif char == '"':
            return self._parse_string()
        elif char == "t" or char == "f" or char == "n":
            return self._parse_literal()
        elif char == "-" or char.isdigit():
            return self._parse_number()
        else:
            raise ValueError(f"Unexpected character: {char}")

    def _parse_object(self) -> dict:
        """Parses a JSON object: { 'key': value, ... }."""
        obj = {}
        self.index += 1  # Skip '{'
        self._skip_whitespace()

        if self.index < self.length and self.json_str[self.index] == "}":
            self.index += 1
            return obj

        while True:
            self._skip_whitespace()
            key = self._parse_string()
            self._skip_whitespace()

            if self.index >= self.length or self.json_str[self.index] != ":":
                raise ValueError("Expected ':' after key in object")
            self.index += 1  # Skip ':'

            value = self._parse_value()
            obj[key] = value

            self._skip_whitespace()
            if self.index < self.length and self.json_str[self.index] == "}":
                self.index += 1
                return obj
            elif self.index < self.length and self.json_str[self.index] == ",":
                self.index += 1
                self._skip_whitespace()
            else:
                raise ValueError("Expected ',' or '}' in object")

    def _parse_array(self) -> list:
        """Parses a JSON array: [ value, ... ]."""
        arr = []
        self.index += 1  # Skip '['
        self._skip_whitespace()

        if self.index < self.length and self.json_str[self.index] == "]":
            self.index += 1
            return arr

        while True:
            arr.append(self._parse_value())
            self._skip_whitespace()

            if self.index < self.length and self.json_str[self.index] == "]":
                self.index += 1
                return arr
            elif self.index < self.length and self.json_str[self.index] == ",":
                self.index += 1
                self._skip_whitespace()
            else:
                raise ValueError("Expected ',' or ']' in array")

    def _parse_string(self) -> str:
        """Parses a JSON string enclosed in double quotes."""
        self.index += 1  # Skip opening '"'
        start = self.index
        while self.index < self.length and self.json_str[self.index] != '"':
            # Note: This implementation assumes no escaped quotes for simplicity,
            # but can be extended to handle \".
            if self.json_str[self.index] == "\\":
                self.index += 1
            self.index += 1

        if self.index >= self.length:
            raise ValueError("Unterminated string")

        result = self.json_str[start:self.index]
        self.index += 1  # Skip closing '"'
        return result

    def _parse_number(self) -> Union[int, float]:
        """Parses a JSON number (integer or float)."""
        start = self.index
        if self.json_str[self.index] == "-":
            self.index += 1

        while self.index < self.length and (self.json_str[self.index].isdigit() or self.json_str[self.index] == "."):
            self.index += 1

        num_str = self.json_str[start:self.index]
        if "." in num_str:
            return float(num_str)
        return int(num_str)

    def _parse_literal(self) -> Union[bool, None]:
        """Parses JSON literals: true, false, null."""
        if self.json_str.startswith("true", self.index):
            self.index += 4
            return True
        elif self.json_str.startswith("false", self.index):
            self.index += 5
            return False
        elif self.json_str.startswith("null", self.index):
            self.index += 4
            return None
        raise ValueError("Invalid literal")

    def parse(self) -> Any:
        """Executes the parsing process."""
        result = self._parse_value()
        self._skip_whitespace()
        if self.index < self.length:
            raise ValueError("Trailing data after JSON object")
        return result


def solve(json_string: str) -> Any:
    """
    Converts a JSON string into its corresponding Python object.

    Args:
        json_string (str): The JSON formatted string to parse.

    Returns:
        Any: The parsed Python object (dict, list, str, int, float, bool, or None).

    Examples:
        >>> solve('{"a": 1, "b": [true, null, "hello"]')
        {'a': 1, 'b': [True, None, 'hello']}
        >>> solve('[1, 2, 3]')
        [1, 2, 3]
    """
    # Initialize the parser with the input string
    parser = JSONParser(json_string)
    # The parse method uses recursive descent to traverse the string
    return parser.parse()
