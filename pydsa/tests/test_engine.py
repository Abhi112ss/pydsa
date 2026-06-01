import pytest
from pydsa.core import registry
from pydsa import search, find
from pydsa.core.exceptions import ProblemNotFoundError, InvalidInputError

def test_registry_loads_successfully():
    """Ensure all generated solver files load without syntax errors."""
    registry._ensure_loaded()
    problems = registry.all_problems()
    # You have 3944 problems. If this drops significantly, files were deleted/broken!
    assert len(problems) > 3900 

def test_search_functionality():
    """Ensure the search system returns valid results."""
    results = search("two sum", limit=5)
    assert len(results) > 0
    assert results[0].id is not None

def test_find_exact_id():
    """Ensure direct ID lookups work."""
    problem = find(1)  # LeetCode ID 1 is usually Two Sum
    assert problem.name == "Two Sum"

def test_invalid_problem_handling():
    """Ensure the engine gracefully rejects garbage queries."""
    from pydsa.core.exceptions import ProblemNotFoundError, AmbiguousQueryError
    
    # The AI brain might throw an Ambiguous error, the text brain throws Not Found. 
    # Both mean the engine successfully rejected the garbage input!
    with pytest.raises((ProblemNotFoundError, AmbiguousQueryError)):
        find("this_problem_definitely_does_not_exist_12345")