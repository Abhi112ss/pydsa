METADATA = {
    "id": 1628,
    "name": "Design an Expression Tree",
    "slug": "design_expression_tree",
    "category": "Design",
    "aliases": [],
    "tags": ["trees", "design", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Design a data structure for an expression tree that supports building the tree and evaluating its value.",
}

class ExpressionNode:
    def __init__(self, value: str, left: "ExpressionNode" = None, right: "ExpressionNode" = None):
        self.value = value
        self.left = left
        self.right = right

class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_tree(self, expression_list: list[str]) -> None:
        """
        Args:
            expression_list: A list of strings representing an expression in postfix notation.

        Returns:
            None
        """
        stack = []
        for token in expression_list:
            if token in ("+", "-", "*", "/"):
                right_operand = stack.pop()
                left_operand = stack.pop()
                new_node = ExpressionNode(token, left_operand, right_operand)
                stack.append(new_node)
            else:
                stack.append(ExpressionNode(token))
        self.root = stack[0]

    def evaluate(self) -> float:
        """
        Args:
            None

        Returns:
            The result of the expression evaluation.
        """
        return self._evaluate_recursive(self.root)

    def _evaluate_recursive(self, node: ExpressionNode) -> float:
        if node.left is None and node.right is None:
            return float(node.value)
        
        left_val = self._evaluate_recursive(node.left)
        right_val = self._evaluate_recursive(node.right)
        
        if node.value == "+":
            return left_val + right_val
        elif node.value == "-":
            return left_val - right_val
        elif node.value == "*":
            return left_val * right_val
        elif node.value == "/":
            return left_val / right_val
        return 0.0

def solve() -> None:
    pass