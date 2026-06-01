METADATA = {
    "id": 819,
    "name": "Most Common Word",
    "slug": "most-common-word",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string_parsing", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Find the most frequent non-banned word in a paragraph after normalizing case and removing punctuation.",
}

import collections
import re

def solve(paragraph: str, banned: list[str]) -> str:
    """
    Args:
        paragraph: A string containing words and punctuation.
        banned: A list of words that should be ignored.

    Returns:
        The most frequent non-banned word in lowercase.
    """
    banned_set = set(banned)
    normalized_paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()
    words = normalized_paragraph.split()
    
    counts = collections.Counter()
    for word in words:
        if word not in banned_set:
            counts[word] += 1
            
    return counts.most_common(1)[0][0]