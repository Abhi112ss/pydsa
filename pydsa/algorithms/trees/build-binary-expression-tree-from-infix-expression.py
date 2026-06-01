METADATA = {
    "id": 1597,
    "name": "Build Binary Expression Tree From Infix Expression",
    "slug": "build-binary-expression-tree-from-infix-expression",
    "category": "Trees",
    "aliases": [],
    "tags": ["stack", "trees", "parsing"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a binary expression tree from a given infix expression string using two stacks.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: str = "", left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(expression: str) -> TreeNode:
    """
    Builds a binary expression tree from an infix expression string.

    The algorithm uses the Shunting-yard inspired approach with two stacks:
    one for operands (nodes) and one for operators. It respects operator 
    precedence and parentheses.

    Args:
        expression: A string representing the infix expression.

    Returns:
        The root node of the constructed binary expression tree.

    Examples:
        >>> solve("(1+2)*3")
        # Returns a tree where '*' is root, left is '+' node, right is '3' node.
    """
    # Precedence mapping for operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # Stacks to hold operands (TreeNodes) and operators (strings)
    nodes_stack: list[TreeNode] = []
    operators_stack: list[str] = []

    def build_sub_tree() -> None:
        """Helper to pop two nodes and one operator to create a new subtree."""
        if len(nodes_stack) < 2 or not operators_stack:
            return
        
        operator = operators_stack.pop()
        right_node = nodes_stack.pop()
        left_node = nodes_stack.pop()
        
        # Create a new internal node with the operator
        new_node = TreeNode(operator, left_node, right_node)
        nodes_stack.append(new_node)

    i = 0
    n = len(expression)
    while i < n:
        char = expression[i]

        if char == ' ':
            i += 1
            continue

        if char == '(':
            operators_stack.append(char)
        elif char == ')':
            # Process everything inside the parentheses
            while operators_stack and operators_stack[-1] != '(':
                build_sub_tree()
            # Pop the '('
            if operators_stack:
                operators_stack.pop()
        elif char in precedence:
            # While the top of the stack has higher or equal precedence, process it
            while (operators_stack and 
                   operators_stack[-1] in precedence and 
                   precedence[operators_stack[-1]] >= precedence[char]):
                build_sub_tree()
            operators_stack.append(char)
        else:
            # It's an operand (number/variable)
            # Handle multi-digit numbers or multi-character operands
            start = i
            while i < n and expression[i] not in precedence and expression[i] not in "() ":
                i += 1
            operand_val = expression[start:i]
            nodes_stack.append(TreeNode(operand_val))
            # Decrement i because the outer loop will increment it, 
            # but we've already advanced past the operand
            i -= 1
        
        i += 1

    # Finalize remaining operations in the stack
    while operators_stack:
        build_sub_tree()

    return nodes_stack[0] if nodes_stack else None
