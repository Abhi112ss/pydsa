METADATA = {
    "id": 2690,
    "name": "Infinite Method Object",
    "slug": "infinite-method-object",
    "category": "Design",
    "aliases": [],
    "tags": ["design_patterns", "object-oriented-programming"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design a class that returns itself when any method is called.",
}

class InfiniteMethodObject:
    """
    A class that implements the infinite method pattern.
    Any method call on an instance of this class returns the instance itself.
    """

    def __getattr__(self, name: str):
        """
        Intercepts any attribute access that is not defined in the class.
        Since any method call is an attribute access, we return self.

        Args:
            name (str): The name of the attribute/method being accessed.

        Returns:
            InfiniteMethodObject: The instance itself to allow chaining.
        """
        # When any method (attribute) is accessed, return the instance itself.
        # This allows for infinite chaining like obj.a().b().c()...
        return self

    def __call__(self):
        """
        Allows the object to be called as a function.
        
        Returns:
            InfiniteMethodObject: The instance itself.
        """
        return self

def solve() -> InfiniteMethodObject:
    """
    Factory function to create an instance of InfiniteMethodObject.

    Returns:
        InfiniteMethodObject: An instance that supports infinite method chaining.

    Examples:
        >>> obj = solve()
        >>> obj.a().b().c()
        <__main__.InfiniteMethodObject object at ...>
    """
    return InfiniteMethodObject()
