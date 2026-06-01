METADATA = {
    "id": 535,
    "name": "Encode and Decode TinyURL",
    "slug": "encode-and-decode-tinyurl",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "design", "string"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design an algorithm to encode a URL to a shortened URL and decode it back to the original URL.",
}

import random
import string

class Codec:
    """
    A class to encode and decode URLs using a hash map and a random key generator.
    """

    def __init__(self) -> None:
        """
        Initializes the Codec with an empty mapping and a base URL.
        """
        self.base_url = "http://tinyurl.com/"
        # Maps the unique short key to the original long URL
        self.url_map: dict[str, str] = {}
        # Set to keep track of used keys to avoid collisions
        self.used_keys: set[str] = set()
        # Character set for generating random keys
        self.alphabet = string.ascii_letters + string.digits

    def encode(self, long_url: str) -> str:
        """
        Encodes a URL to a shortened URL.

        Args:
            long_url: The original long URL string.

        Returns:
            The shortened URL string.

        Examples:
            >>> codec = Codec()
            >>> codec.encode("https://leetcode.com/problems/design-tinyurl/")
            'http://tinyurl.com/aB3dE9'
        """
        # Generate a unique 6-character key
        while True:
            key = "".join(random.choices(self.alphabet, k=6))
            if key not in self.used_keys:
                break
        
        self.used_keys.add(key)
        self.url_map[key] = long_url
        return self.base_url + key

    def decode(self, short_url: str) -> str:
        """
        Decodes a shortened URL to its original URL.

        Args:
            short_url: The shortened URL string.

        Returns:
            The original long URL string.

        Examples:
            >>> codec = Codec()
            >>> short = codec.encode("https://leetcode.com")
            >>> codec.decode(short)
            'https://leetcode.com'
        """
        # Extract the key from the end of the short URL
        # The key starts after the base_url length
        key = short_url.replace(self.base_url, "")
        
        # Retrieve the original URL from the map
        return self.url_map.get(key, "")

def solve() -> None:
    """
    Test function to demonstrate the functionality of the Codec class.
    """
    codec = Codec()
    test_urls = [
        "https://leetcode.com/problems/design-tinyurl/",
        "https://www.google.com",
        "https://github.com/trending",
        "http://a.b"
    ]

    for url in test_urls:
        shortened = codec.encode(url)
        decoded = codec.decode(shortened)
        print(f"Original: {url}")
        print(f"Shortened: {shortened}")
        print(f"Decoded: {decoded}")
        assert url == decoded, f"Error: Expected {url}, got {decoded}"
        print("-" * 20)
