METADATA = {
    "id": 661,
    "name": "Image Smoother",
    "slug": "image_smoother",
    "category": "Array",
    "aliases": [],
    "tags": ["matrix", "simulation"],
    "difficulty": "Easy",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Smooth each pixel by averaging it with its surrounding neighbors."
}


def solve(image: list[list[int]]) -> list[list[int]]:
    """Smooth the given image by averaging each pixel with its valid neighbors.

    Args:
        image: A 2‑D list of integers representing the grayscale values of the image.
               The dimensions are m rows by n columns, where 1 ≤ m, n ≤ 200.

    Returns:
        A new 2‑D list of the same dimensions where each element is the floor of the
        average of the original element and all of its surrounding neighbors
        (including diagonals) that lie within the image bounds.

    Examples:
        >>> solve([[1,2,3],[4,5,6],[7,8,9]])
        [[3, 3, 4], [4, 5, 6], [6, 6, 7]]
        >>> solve([[100,200,100],[200,50,200],[100,200,100]])
        [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
    """
    row_count: int = len(image)
    column_count: int = len(image[0]) if row_count > 0 else 0

    # Prepare result matrix with the same dimensions
    smoothed_image: list[list[int]] = [[0] * column_count for _ in range(row_count)]

    for i in range(row_count):
        for j in range(column_count):
            neighbor_sum: int = 0
            neighbor_count: int = 0

            # Iterate over the 3x3 window centered at (i, j)
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    neighbor_row: int = i + dr
                    neighbor_col: int = j + dc

                    # Check if neighbor coordinates are within bounds
                    if 0 <= neighbor_row < row_count and 0 <= neighbor_col < column_count:
                        neighbor_sum += image[neighbor_row][neighbor_col]
                        neighbor_count += 1

            # Floor division gives the required integer average
            smoothed_image[i][j] = neighbor_sum // neighbor_count

    return smoothed_image