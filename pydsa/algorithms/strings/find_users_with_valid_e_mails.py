METADATA = {
    "id": 1517,
    "name": "Find Users With Valid E-Mails",
    "slug": "find-users-with-valid-e-mails",
    "category": "String",
    "aliases": [],
    "tags": ["regex", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a list of emails, return those that follow a specific valid format using regular expressions.",
}

import re

def solve(emails: list[str]) -> list[str]:
    """
    Filters a list of emails based on specific validity criteria using regex.

    Criteria:
    1. The prefix must start with a letter.
    2. The prefix can contain letters (upper/lower), digits, underscore, period, and dash.
    3. The prefix cannot contain two consecutive periods.
    4. The domain must be a valid domain (e.g., gmail.com, facebook.com).
    5. The domain must be a valid domain name (letters, digits, hyphen) followed by a dot and a suffix.
    6. The suffix must be at least 2 characters long and consist only of letters.

    Args:
        emails: A list of strings representing email addresses.

    Returns:
        A list of valid email strings, sorted lexicographically.

    Examples:
        >>> solve(["test.email@leetcode.com", "test@leetcode.com", "test.@leetcode.com", "test..email@leetcode.com"])
        ['test.email@leetcode.com', 'test@leetcode.com']
    """
    # Regex breakdown:
    # ^[a-zA-Z]             : Starts with a letter
    # [a-zA-Z0-9._-]*       : Followed by any number of allowed characters
    # (?<!\.)               : Negative lookbehind to ensure the character before '@' is not a period
    # @                     : Literal '@'
    # [a-zA-Z0-9-]+         : Domain name (letters, digits, hyphens)
    # \.                    : Literal dot
    # [a-zA-Z]{2,}$         : Suffix of at least 2 letters at the end of the string
    # Note: To handle the "no consecutive periods" rule, we use a lookahead or specific pattern.
    # A more robust way to handle "no consecutive periods" in the prefix is:
    # ^[a-zA-Z]([a-zA-Z0-9._-]*[a-zA-Z0-9_-])?  <-- This is complex.
    # Let's use: ^[a-zA-Z][a-zA-Z0-9._-]*@... 
    # and then check for '..' in the prefix part.
    
    # Refined Regex:
    # 1. ^[a-zA-Z] : Starts with letter
    # 2. (?!.*\.{2,}) : Negative lookahead to ensure no two consecutive dots exist anywhere in the prefix
    # 3. [a-zA-Z0-9._-]* : Allowed characters in prefix
    # 4. (?<!\.)@ : Ensure the character before @ is not a dot
    # 5. [a-zA-Z0-9-]+ : Domain name
    # 6. \.[a-zA-Z]{2,}$ : Dot followed by 2+ letters suffix
    
    pattern = re.compile(r"^[a-zA-Z](?!.*\.{2,})[a-zA-Z0-9._-]*[a-zA-Z0-9_-]?@(?<!\.)[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
    
    # However, the requirement "prefix cannot contain two consecutive periods" 
    # and "prefix cannot end with a period" can be simplified.
    # Let's use a pattern that explicitly handles the prefix constraints.
    
    # Corrected Pattern:
    # ^[a-zA-Z]             -> Starts with letter
    # (?!.*\.{2,})          -> No consecutive dots in the whole string (effectively prefix)
    # [a-zA-Z0-9._-]*       -> Allowed prefix chars
    # (?<!\.)               -> Prefix does not end with dot (lookbehind before @)
    # @                     -> The @ symbol
    # [a-zA-Z0-9-]+         -> Domain name
    # \.                    -> The dot
    # [a-zA-Z]{2,}$         -> Suffix (2+ letters)
    
    # Re-evaluating the "prefix cannot end with dot" logic:
    # The regex below ensures:
    # 1. Starts with letter.
    # 2. No '..' anywhere.
    # 3. The character immediately before '@' is not '.'.
    # 4. Domain is alphanumeric/hyphen.
    # 5. Suffix is 2+ letters.
    
    regex_pattern = r"^[a-zA-Z](?!.*\.{2,})[a-zA-Z0-9._-]*[a-zA-Z0-9_-]@(?<!\.)[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    # Wait, the prefix could be just one letter (e.g., a@b.com). 
    # The [a-zA-Z0-9_-]@ part requires at least one char after the first letter.
    # Let's use a more flexible approach for the prefix.
    
    valid_emails = []
    
    # Final robust pattern:
    # ^[a-zA-Z]             : Starts with letter
    # (?!.*\.{2,})          : No consecutive dots
    # [a-zA-Z0-9._-]*       : Prefix characters
    # (?<!\.)               : Prefix does not end with dot
    # @                     : Literal @
    # [a-zA-Z0-9-]+         : Domain
    # \.                    : Literal dot
    # [a-zA-Z]{2,}$         : Suffix
    
    final_pattern = re.compile(r"^[a-zA-Z](?!.*\.{2,})[a-zA-Z0-9._-]*[a-zA-Z0-9_-]?@(?<!\.)[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")
    # Note: The (?<!\.) lookbehind is applied to the character before '@'. 
    # But in Python re, lookbehinds must be fixed width. 
    # Since '@' is a single char, (?<!\.)@ works.
    
    # Let's refine the pattern one last time to be strictly compliant with LeetCode's edge cases:
    # 1. Start with letter: ^[a-zA-Z]
    # 2. No consecutive dots: (?!.*\.{2,})
    # 3. Prefix chars: [a-zA-Z0-9._-]*
    # 4. Prefix doesn't end with dot: (?<!\.)@
    # 5. Domain: [a-zA-Z0-9-]+
    # 6. Suffix: \.[a-zA-Z]{2,}$
    
    # Because of the fixed-width constraint on lookbehind, we use:
    # ^[a-zA-Z](?!.*\.{2,})[a-zA-Z0-9._-]*[a-zA-Z0-9_-]@... is too restrictive for single char prefixes.
    # Let's use:
    # ^[a-zA-Z][a-zA-Z0-9._-]*@... and then check the dot constraints manually or via lookahead.
    
    # The most reliable regex for this specific problem:
    # ^[a-zA-Z]             : Start with letter
    # (?!.*\.{2,})          : No consecutive dots
    # [a-zA-Z0-9._-]*       : Prefix chars
    # (?<!\.)               : Not ending in dot (lookbehind)
    # @                     : @
    # [a-zA-Z0-9-]+         : Domain
    # \.                    : Dot
    # [a-zA-Z]{2,}$         : Suffix
    
    # To handle the "prefix cannot end with dot" without fixed-width issues:
    # We can use a lookahead at the start: ^(?=[a-zA-Z])(?!.*\.{2,})(?!.*\.@)[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$
    # Breakdown:
    # ^(?=[a-zA-Z])         : Lookahead to ensure first char is a letter
    # (?!.*\.{2,})          : Lookahead to ensure no consecutive dots
    # (?!.*\.@)             : Lookahead to ensure no dot before @
    # [a-zA-Z0-9._-]+       : Match the prefix
    # @                     : Match @
    # [a-zA-Z0-9-]+         : Match domain
    # \.                    : Match dot
    # [a-zA-Z]{2,}$         : Match suffix
    
    pattern = re.compile(r"^[a-zA-Z](?!.*\.{2,})(?!.*\.@)[a-zA-Z0-9._-]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$")

    for email in emails:
        # Check if the email matches the compiled regex pattern
        if pattern.match(email):
            valid_emails.append(email)
            
    # Return the valid emails sorted lexicographically
    return sorted(valid_emails)
