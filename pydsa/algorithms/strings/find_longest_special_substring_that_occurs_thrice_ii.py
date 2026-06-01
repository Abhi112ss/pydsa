METADATA = {
    "id": 2982,
    "name": "Find Longest Special Substring That Occurs Thrice II",
    "slug": "find_longest_special_substring_that_occurs_thrice_ii",
    "category": "String",
    "aliases": [],
    "tags": ["suffix_automaton", "suffix_array", "string_matching"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the longest substring that appears at least three times in a given string.",
}

class SuffixAutomaton:
    """
    A Suffix Automaton (SAM) implementation to find substring frequencies.
    """
    def __init__(self, s: str):
        self.nodes = [{"len": 0, "link": -1, "next": {}, "count": 0}]
        self.last = 0
        for char in s:
            self._extend(char)
        self._calculate_counts()

    def _extend(self, char: str) -> None:
        cur = len(self.nodes)
        self.nodes.append({"len": self.nodes[self.last]["len"] + 1, "link": 0, "next": {}, "count": 1})
        p = self.last
        while p != -1 and char not in self.nodes[p]["next"]:
            self.nodes[p]["next"][char] = cur
            p = self.nodes[p]["link"]
        
        if p == -1:
            self.nodes[cur]["link"] = 0
        else:
            q = self.nodes[p]["next"][char]
            if self.nodes[p]["len"] + 1 == self.nodes[q]["len"]:
                self.nodes[cur]["link"] = q
            else:
                clone = len(self.nodes)
                self.nodes.append({
                    "len": self.nodes[p]["len"] + 1,
                    "link": self.nodes[q]["link"],
                    "next": self.nodes[q]["next"].copy(),
                    "count": 0  # Clones don't represent new end positions
                })
                while p != -1 and self.nodes[p]["next"].get(char) == q:
                    self.nodes[p]["next"][char] = clone
                    p = self.nodes[p]["link"]
                self.nodes[q]["link"] = clone
                self.nodes[cur]["link"] = clone
        self.last = cur

    def _calculate_counts(self) -> None:
        # Sort nodes by length in descending order to propagate counts up the suffix link tree
        sorted_indices = sorted(range(len(self.nodes)), key=lambda i: self.nodes[i]["len"], reverse=True)
        for i in sorted_indices:
            link = self.nodes[i]["link"]
            if link != -1:
                self.nodes[link]["count"] += self.nodes[i]["count"]

def solve(s: str) -> str:
    """
    Finds the longest substring that occurs at least three times in the string s.

    Args:
        s: The input string.

    Returns:
        The longest substring occurring at least three times. If multiple exist, 
        the one appearing earliest is returned (though problem usually implies any).
        Returns an empty string if no such substring exists.

    Examples:
        >>> solve("aaaaa")
        'aaa'
        >>> solve("abcabcabc")
        'abc'
        >>> solve("abcdef")
        ''
    """
    if not s:
        return ""

    sam = SuffixAutomaton(s)
    
    max_len = 0
    best_end_pos = -1

    # We need to find the longest substring with count >= 3.
    # In SAM, each node represents a set of substrings. 
    # The longest substring in node 'i' has length nodes[i]['len'].
    # All substrings in node 'i' occur 'nodes[i]['count']' times.
    
    # To reconstruct the string, we need to know where a node occurs.
    # We can track the first end position during construction.
    
    # Re-running construction with end-position tracking for reconstruction
    nodes = [{"len": 0, "link": -1, "next": {}, "count": 0, "first_pos": -1}]
    last = 0
    for idx, char in enumerate(s):
        cur = len(nodes)
        nodes.append({"len": nodes[last]["len"] + 1, "link": 0, "next": {}, "count": 1, "first_pos": idx})
        p = last
        while p != -1 and char not in nodes[p]["next"]:
            nodes[p]["next"][char] = cur
            p = nodes[p]["link"]
        if p == -1:
            nodes[cur]["link"] = 0
        else:
            q = nodes[p]["next"][char]
            if nodes[p]["len"] + 1 == nodes[q]["len"]:
                nodes[cur]["link"] = q
            else:
                clone = len(nodes)
                nodes.append({
                    "len": nodes[p]["len"] + 1,
                    "link": nodes[q]["link"],
                    "next": nodes[q]["next"].copy(),
                    "count": 0,
                    "first_pos": nodes[q]["first_pos"] # Clone inherits end position
                })
                while p != -1 and nodes[p]["next"].get(char) == q:
                    nodes[p]["next"][char] = clone
                    p = nodes[p]["link"]
                nodes[q]["link"] = clone
                nodes[cur]["link"] = clone
        last = cur

    # Propagate counts
    sorted_indices = sorted(range(len(nodes)), key=lambda i: nodes[i]["len"], reverse=True)
    for i in sorted_indices:
        link = nodes[i]["link"]
        if link != -1:
            nodes[link]["count"] += nodes[i]["count"]

    # Find the node with count >= 3 and maximum length
    best_len = 0
    best_end = -1
    
    for i in range(1, len(nodes)):
        if nodes[i]["count"] >= 3:
            if nodes[i]["len"] > best_len:
                best_len = nodes[i]["len"]
                best_end = nodes[i]["first_pos"]
            elif nodes[i]["len"] == best_len:
                # If lengths are equal, we don't strictly need to handle tie-breaking 
                # unless specified, but usually, we pick the first one.
                pass

    if best_end == -1:
        return ""
    
    return s[best_end - best_len + 1 : best_end + 1]
