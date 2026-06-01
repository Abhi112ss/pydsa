METADATA = {
    "id": 1612,
    "name": "Check If Two Expression Trees are Equivalent",
    "slug": "check-if-two-expression-trees-are-equivalent",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if two expression trees represent the same mathematical expression by evaluating their values.",
}

class ExpressionTree:
    def __init__(self, val: str, left: 'ExpressionTree' = None, right: 'ExpressionTree' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(expressionTree1: ExpressionTree, expressionTree2: ExpressionTree) -> bool:
    """
    Args:
        expressionTree1: The root of the first expression tree.
        expressionTree2: The root of the second expression tree.

    Returns:
        True if the two expression trees are equivalent, False otherwise.
    """
    def evaluate(node: ExpressionTree) -> int:
        if node.left is None and node.right is None:
            return int(node.val)
        
        left_value = evaluate(node.left)
        right_value = evaluate(node.right)
        
        if node.val == '+':
            return left_value + right_value
        elif node.val == '-':
            return left_value - right_value
        elif node.val == '*':
            return left_value * right_value
        elif node.val == '/':
            return left_value // right_value
        return 0

    return evaluate(expressionTree1) == evaluate(expressionTree2)