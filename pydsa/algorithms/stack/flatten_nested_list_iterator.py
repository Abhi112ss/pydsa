METADATA = {
    "id": 341,
    "name": "Flatten Nested List Iterator",
    "slug": "flatten-nested-list-iterator",
    "category": "Design",
    "aliases": [],
    "tags": ["stack", "design", "iterator", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(1) average for next/hasNext, O(N) space",
    "space_complexity": "O(N)",
    "description": "Implement an iterator to flatten a nested list of integers.",
}

class NestedInteger:
    """
    This is the interface that allows you to nest integers and lists.
    You should not implement it, or speculate about its implementation.
    """
    def isInteger(self) -> bool:
        """@return True if this NestedInteger holds a single integer, rather than a nested list."""
        pass

    def getInteger(self) -> int:
        """@return the integer if this NestedInteger holds a single integer, rather than a nested list."""
        pass

    def getList(self) -> list['NestedInteger']:
        """@return the nested list if this NestedInteger holds a nested list, rather than a single integer."""
        pass


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        """
        Initializes the iterator with a nested list.

        Args:
            nestedList: A list of NestedInteger objects.
        """
        # We use a stack to keep track of the elements. 
        # We store them in reverse order so that the first element is at the top of the stack.
        self.stack: list[NestedInteger] = nestedList[::-1]

    def next(self) -> int:
        """
        Returns the next integer in the flattened list.

        Returns:
            The next integer.

        Raises:
            StopIteration: If there are no more integers.
        """
        # hasNext() is guaranteed to be called before next() per LeetCode contract,
        # and hasNext() ensures the top of the stack is an integer.
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        """
        Returns True if there are still integers in the iterator.

        Returns:
            True if next() can be called, False otherwise.
        """
        # We process the stack until the top element is an integer.
        # This handles nested lists of any depth.
        while self.stack:
            top_element = self.stack[-1]
            
            if top_element.isInteger():
                return True
            
            # If the top element is a list, pop it and push its contents onto the stack in reverse.
            # This ensures we process the list elements in the correct order (left to right).
            self.stack.pop()
            nested_list = top_element.getList()
            for i in range(len(nested_list) - 1, -1, -1):
                self.stack.append(nested_list[i])
                
        return False

def solve():
    """
    Example usage of the NestedIterator.
    """
    pass
