METADATA = {
    "id": 1181,
    "name": "Before and After Puzzle",
    "slug": "before-and-after-puzzle",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 * L)",
    "space_complexity": "O(n * L)",
    "description": "Find the maximum number of phrases that can be formed by concatenating the end of one phrase with the beginning of another.",
}

def solve(phrases: list[str]) -> int:
    """
    Args:
        phrases: A list of strings representing phrases.

    Returns:
        The maximum number of phrases that can be formed.
    """
    if not phrases:
        return 0

    phrase_data = []
    for phrase in phrases:
        parts = phrase.split()
        phrase_data.append((parts[0], parts[-1]))

    n = len(phrase_data)
    max_count = 0

    for i in range(n):
        current_count = 1
        used_indices = {i}
        last_word = phrase_data[i][1]

        while True:
            best_next_index = -1
            for j in range(n):
                if j not in used_indices and phrase_data[j][0] == last_word:
                    best_next_index = j
                    break
            
            if best_next_index != -1:
                current_count += 1
                used_indices.add(best_next_index)
                last_word = phrase_data[best_next_index][1]
            else:
                break
        
        if current_count > max_count:
            max_count = current_count

    return max_count