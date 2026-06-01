METADATA = {
    "id": 756,
    "name": "Pyramid Transition Matrix",
    "slug": "pyramid-transition-matrix",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "backtracking", "memoization", "dynamic programming"],
    "difficulty": "hard",
    "time_complexity": "O(A^N)",
    "space_complexity": "O(N^2)",
    "description": "Determine if a pyramid can be constructed from a given set of blocks by checking all possible transitions between levels.",
}

def solve(blocks: list[int], rows: int) -> bool:
    """
    Args:
        blocks: A list of integers representing the values of the available blocks.
        rows: The number of rows in the pyramid.

    Returns:
        A boolean indicating whether a valid pyramid can be constructed.
    """
    memo = {}

    def can_build(current_row_index: int, current_row_values: tuple[int, ...]) -> bool:
        if current_row_index == rows:
            return True

        state = (current_row_index, current_row_values)
        if state in memo:
            return memo[state]

        num_blocks_needed = rows - current_row_index
        
        def backtrack(block_idx: int, current_combination: list[int]) -> bool:
            if len(current_combination) == num_blocks_needed:
                next_row_values = []
                for i in range(len(current_combination) - 1):
                    next_row_values.append(current_combination[i] + current_combination[i + 1])
                
                if can_build(current_row_index + 1, tuple(next_row_values)):
                    return True
                return False

            for i in range(block_idx, len(blocks)):
                current_combination.append(blocks[i])
                if backtrack(i + 1, current_combination):
                    return True
                current_combination.pop()
            
            return False

        result = backtrack(0, [])
        memo[state] = result
        return result

    def find_initial_combinations(block_idx: int, current_combination: list[int]) -> bool:
        if len(current_combination) == rows:
            if can_build(1, tuple(current_combination)):
                return True
            return False

        for i in range(block_idx, len(blocks)):
            current_combination.append(blocks[i])
            if find_initial_combinations(i + 1, current_combination):
                return True
            current_combination.pop()
        
        return False

    return find_initial_combinations(0, [])