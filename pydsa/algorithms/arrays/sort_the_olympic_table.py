METADATA = {
    "id": 2377,
    "name": "Sort the Olympic Table",
    "slug": "sort-the-olympic-table",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort countries based on gold, silver, and bronze medal counts in descending order, then by name in ascending order.",
}

from functools import cmp_to_key

def solve(countries: list[list[str]]) -> list[list[str]]:
    """
    Sorts the Olympic table based on medal counts and country names.

    The sorting criteria are:
    1. Gold medals (descending)
    2. Silver medals (descending)
    3. Bronze medals (descending)
    4. Country name (ascending/alphabetical)

    Args:
        countries: A list of lists, where each sublist contains 
                   [country_name, gold, silver, bronze].

    Returns:
        A list of lists sorted according to the Olympic rules.

    Examples:
        >>> solve([["USA", "10", "5", "2"], ["China", "10", "5", "3"], ["Japan", "5", "5", "5"]])
        [['China', '10', '5', '3'], ['USA', '10', '5', '2'], ['Japan', '5', '5', '5']]
    """

    def compare_countries(country_a: list[str], country_b: list[str]) -> int:
        """
        Custom comparator for sorting countries.
        """
        # Extract medal counts and convert to integers for comparison
        gold_a, silver_a, bronze_a = int(country_a[1]), int(country_a[2]), int(country_a[3])
        gold_b, silver_b, bronze_b = int(country_b[1]), int(country_b[2]), int(country_b[3])

        # 1. Compare Gold medals (Descending)
        if gold_a != gold_b:
            return gold_b - gold_a
        
        # 2. Compare Silver medals (Descending)
        if silver_a != silver_b:
            return silver_b - silver_a
        
        # 3. Compare Bronze medals (Descending)
        if bronze_a != bronze_b:
            return bronze_b - bronze_a
        
        # 4. Compare Names (Ascending/Lexicographical)
        if country_a[0] < country_b[0]:
            return -1
        elif country_a[0] > country_b[0]:
            return 1
        else:
            return 0

    # Use cmp_to_key to transform our comparator into a key function for sort()
    # Python's Timsort is O(n log n) and stable.
    return sorted(countries, key=cmp_to_key(compare_countries))
