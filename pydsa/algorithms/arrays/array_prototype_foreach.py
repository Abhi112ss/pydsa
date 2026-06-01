METADATA = {
    "id": 2804,
    "name": "Array Prototype ForEach",
    "slug": "array-prototype-foreach",
    "category": "Implementation",
    "aliases": [],
    "tags": ["arrays", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Implement the forEach method for arrays which executes a provided callback function once for each array element.",
}

from typing import Any, Callable, List


class ArrayPrototype:
    """
    A class to simulate the behavior of the JavaScript Array prototype.
    """

    def for_each(
        self, 
        callback: Callable[[Any, int, List[Any]], None], 
        this_arg: Any = None
    ) -> None:
        """
        Executes a provided function once for each array element.

        Args:
            callback: A function that is called for every element in the array. 
                The function should take three arguments: 
                (current_value, index, array).
            this_arg: Value to use as 'this' when executing callback.

        Returns:
            None

        Examples:
            >>> arr = ArrayPrototype()
            >>> arr.data = [1, 2, 3]
            >>> result = []
            >>> arr.for_each(lambda val, idx, arr: result.append(val * 2))
            >>> result
            [2, 4, 6]
        """
        # In a real JS environment, 'this' refers to the array instance.
        # We assume the array data is stored in an attribute named 'data'.
        array_data = getattr(self, "data", [])
        
        # Iterate through the array using indices to match the callback signature
        for index in range(len(array_data)):
            # The callback is called with (element, index, original_array)
            # If this_arg is provided, it would be used as the context for the call
            # In Python, we simulate this by passing it if the callback is a method,
            # but for standard functions, we simply call it.
            callback(array_data[index], index, array_data)


def solve(nums: List[Any], callback: Callable[[Any, int, List[Any]], None]) -> None:
    """
    Wrapper function to match the LeetCode problem signature.

    Args:
        nums: The input list of elements.
        callback: The function to execute for each element.

    Returns:
        None
    """
    # Create an instance of our prototype simulator
    prototype = ArrayPrototype()
    # Assign the input list to the internal data attribute
    prototype.data = nums
    # Execute the for_each method
    prototype.for_each(callback)
