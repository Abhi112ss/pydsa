METADATA = {
    "id": 736,
    "name": "Parse Lisp Expression",
    "slug": "parse-lisp-expression",
    "category": "String",
    "aliases": [],
    "tags": ["recursion", "hash_map", "string_parsing"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Evaluate a Lisp-like expression with variable bindings and nested scopes.",
}

class LispParser:
    def __init__(self, expression: str):
        self.expression = expression
        self.index = 0

    def parse(self, scope: dict[str, int]) -> int:
        """
        Parses and evaluates the Lisp expression starting from the current index.

        Args:
            scope: A dictionary mapping variable names to their integer values.

        Returns:
            The integer result of the evaluated expression.

        Examples:
            >>> parser = LispParser("(let (x 5) (let (y 2) (+ x y)))")
            >>> parser.parse({})
            7
        """
        # Skip whitespace
        self._skip_whitespace()

        if self.expression[self.index] != '(':
            # Base case: The expression is a single integer or a variable
            token = self._get_token()
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                return int(token)
            return scope[token]

        # Recursive case: The expression is a list starting with '('
        self.index += 1  # Skip '('
        self._skip_whitespace()

        # Determine the operation type
        operation = self._get_token()

        if operation == "let":
            # Handle (let (var val) ...)
            # First, parse the bindings list: (x 5 y 2)
            self._skip_whitespace()
            if self.expression[self.index] == '(':
                self.index += 1  # Skip '(' of bindings
                new_scope = scope.copy()
                while self.expression[self.index] != ')':
                    var_name = self._get_token()
                    self._skip_whitespace()
                    var_value = self.parse(new_scope) # This handles nested expressions in let
                    new_scope[var_name] = var_value
                    self._skip_whitespace()
                self.index += 1  # Skip ')' of bindings
            
            # After bindings, parse the body expression
            result = self.parse(new_scope)
            self._skip_whitespace()
            self.index += 1  # Skip ')' of let
            return result

        elif operation in ("+", "-", "*"):
            # Handle arithmetic operations: (+ expr1 expr2 ...)
            values = []
            while True:
                self._skip_whitespace()
                if self.expression[self.index] == ')':
                    break
                values.append(self.parse(scope))
            
            self.index += 1  # Skip ')'
            
            if operation == "+":
                return sum(values)
            elif operation == "-":
                # Subtraction is left-associative: (- 10 2 3) -> (10 - 2) - 3 = 5
                res = values[0]
                for i in range(1, len(values)):
                    res -= values[i]
                return res
            else:  # "*"
                res = 1
                for val in values:
                    res *= val
                return res
        
        return 0

    def _skip_whitespace(self) -> None:
        while self.index < len(self.expression) and self.expression[self.index].isspace():
            self.index += 1

    def _get_token(self) -> str:
        """Extracts the next contiguous non-space token."""
        start = self.index
        while self.index < len(self.expression) and not self.expression[self.index].isspace() and self.expression[self.index] not in "()":
            self.index += 1
        return self.expression[start:self.index]


def solve(expression: str) -> int:
    """
    Evaluates the given Lisp expression.

    Args:
        expression: A string representing the Lisp expression.

    Returns:
        The integer result of the expression.
    """
    parser = LispParser(expression)
    return parser.parse({})
