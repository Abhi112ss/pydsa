METADATA = {
    "id": 460,
    "name": "LFU Cache",
    "slug": "lfu-cache",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "doubly_linked_list", "design"],
    "difficulty": "hard",
    "time_complexity": "O(1)",
    "space_complexity": "O(capacity)",
    "description": "Design and implement a Least Frequently Used (LFU) cache system that supports get and put operations in constant time.",
}

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self) -> Node:
        if self.size == 0:
            return None
        last_node = self.tail.prev
        self.remove_node(last_node)
        return last_node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_map = {}
        self.freq_map = {}

    def _update_node(self, node: Node):
        old_freq = node.freq
        self.freq_map[old_freq].remove_node(node)
        
        if self.freq_map[old_freq].size == 0 and self.min_freq == old_freq:
            self.min_freq += 1
            
        node.freq += 1
        new_freq = node.freq
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].add_to_front(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._update_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._update_node(node)
            return

        if self.size >= self.capacity:
            lfu_list = self.freq_map[self.min_freq]
            removed_node = lfu_list.remove_tail()
            if removed_node:
                del self.key_map[removed_node.key]
                self.size -= 1

        new_node = Node(key, value)
        self.key_map[key] = new_node
        self.min_freq = 1
        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()
        self.freq_map[1].add_to_front(new_node)
        self.size += 1

def solve():
    pass