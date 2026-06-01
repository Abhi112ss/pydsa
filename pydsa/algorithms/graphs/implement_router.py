METADATA = {
    "id": 3508,
    "name": "Implement Router",
    "slug": "implement_router",
    "category": "Design",
    "aliases": [],
    "tags": ["trie", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(L) per operation",
    "space_complexity": "O(N * L)",
    "description": "Implement a router that supports adding IP prefixes and finding the longest prefix match for a given IP address.",
}

class TrieNode:
    """A node in the Trie structure representing a bit or character in a prefix."""
    def __init__(self):
        self.children: dict[int, TrieNode] = {}
        self.is_end_of_prefix: bool = False
        self.value: str = ""

class Router:
    """
    A router implementation using a Trie to perform Longest Prefix Matching (LPM).
    """

    def __init__(self) -> None:
        """Initializes the router with an empty Trie root."""
        self.root = TrieNode()

    def add_prefix(self, prefix: str, value: str) -> None:
        """
        Adds a prefix and its associated value to the routing table.

        Args:
            prefix: The IP prefix string (e.g., "192.168.1.0/24").
            value: The destination or gateway associated with this prefix.
        """
        # Extract the bit string from the prefix (assuming standard CIDR notation)
        # For the sake of a generic Trie implementation, we treat the prefix as a sequence of bits.
        # In a real-world scenario, we would convert the IP to a 32-bit integer.
        bits = self._ip_to_bits(prefix)
        
        current_node = self.root
        for bit in bits:
            if bit not in current_node.children:
                current_node.children[bit] = TrieNode()
            current_node = current_node.children[bit]
        
        # Mark the end of the prefix and store the value
        current_node.is_end_of_prefix = True
        current_node.value = value

    def find_longest_prefix(self, ip: str) -> str:
        """
        Finds the value associated with the longest prefix that matches the given IP.

        Args:
            ip: The IP address to match.

        Returns:
            The value of the longest matching prefix, or an empty string if no match is found.
        """
        bits = self._ip_to_bits(ip, is_full_ip=True)
        current_node = self.root
        longest_match_value = ""

        for bit in bits:
            if bit in current_node.children:
                current_node = current_node.children[bit]
                # If this node marks the end of a known prefix, update our best match
                if current_node.is_end_of_prefix:
                    longest_match_value = current_node.value
            else:
                # No further path in Trie matches the IP bits
                break
        
        return longest_match_value

    def _ip_to_bits(self, ip_str: str, is_full_ip: bool = False) -> str:
        """
        Helper to convert CIDR or IP string into a string of bits.
        
        Args:
            ip_str: The IP or CIDR string.
            is_full_ip: Whether to treat the input as a full 32-bit IP.
            
        Returns:
            A string of '0's and '1's.
        """
        if "/" in ip_str:
            address_part, mask_part = ip_str.split("/")
            mask_len = int(mask_part)
        else:
            address_part = ip_str
            mask_len = 32 if is_full_ip else None

        # Convert IP octets to 32-bit binary string
        octets = address_part.split(".")
        bit_string = "".join(bin(int(octet))[2:].zfill(8) for octet in octets)
        
        # Return only the bits specified by the mask
        return bit_string[:mask_len] if mask_len is not None else bit_string

def solve() -> None:
    """
    Example usage of the Router class.
    """
    router = Router()
    
    # Adding prefixes
    router.add_prefix("192.168.1.0/24", "Gateway_A")
    router.add_prefix("192.168.0.0/16", "Gateway_B")
    router.add_prefix("10.0.0.0/8", "Gateway_C")
    
    # Test cases
    # 1. Should match 192.168.1.0/24 (Longest match)
    print(f"Match 192.168.1.5: {router.find_longest_prefix('192.168.1.5')}") 
    
    # 2. Should match 192.168.0.0/16 (Since 192.168.1.5 doesn't match /24 if it were different)
    # Let's test an IP that matches /16 but not /24
    print(f"Match 192.168.2.5: {router.find_longest_prefix('192.168.2.5')}")
    
    # 3. Should match 10.0.0.0/8
    print(f"Match 10.5.5.5: {router.find_longest_prefix('10.5.5.5')}")
    
    # 4. Should match nothing
    print(f"Match 172.16.0.1: {router.find_longest_prefix('172.16.0.1')}")
