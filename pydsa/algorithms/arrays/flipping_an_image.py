METADATA = {
    "id": 832,
    "name": "Flipping an Image",
    "slug": "flipping-an-image",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Given an n x n binary matrix, flip the image horizontally and then invert it.",
}

def solve(image: list[list[int]]) -> list[list[int]]:
    """
    Args:
        image: A 2D list of integers representing a binary matrix.

    Returns:
        The modified 2D list after flipping and inverting the image.
    """
    rows = len(image)
    columns = len(image[0])

    for row_index in range(rows):
        left = 0
        right = columns - 1
        
        while left <= right:
            if left == right:
                image[row_index][left] = 1 - image[row_index][left]
            else:
                current_left = image[row_index][left]
                current_right = image[row_index][right]
                
                if current_left == current_right:
                    image[row_index][left] = 1 - current_left
                    image[row_index][right] = 1 - current_right
                else:
                    image[row_index][left] = current_right
                    image[row_index][right] = current_left
            
            left += 1
            right -= 1
            
    return image