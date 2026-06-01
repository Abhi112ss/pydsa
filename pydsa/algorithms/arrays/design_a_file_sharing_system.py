METADATA = {
    "id": 1500,
    "name": "Design a File Sharing System",
    "slug": "design_a_file_sharing_system",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "heap", "trees", "sorted_containers"],
    "difficulty": "hard",
    "time_complexity": "O(log N)",
    "space_complexity": "O(N)",
    "description": "Design a system to manage files with popularity-based retrieval and ID-based ordering.",
}

from sortedcontainers import SortedList

class FileSharingSystem:
    """
    A system to manage files, tracking their popularity and providing 
    efficient retrieval based on popularity and file ID.
    
    Note: Since standard Python does not have a built-in Balanced BST like 
    std::set in C++, we use SortedList from the sortedcontainers library 
    conceptually. In a pure stdlib environment, one would implement a 
    SkipList or a Treap. For the purpose of this implementation, we 
    assume the availability of a sorted structure to maintain O(log N).
    """

    def __init__(self):
        # Maps file_id -> popularity
        self.file_to_popularity: dict[int, int] = {}
        
        # Stores tuples of (-popularity, file_id) to allow O(log N) 
        # retrieval of highest popularity, then smallest ID.
        # We use -popularity to simulate a max-heap behavior in a sorted list.
        self.sorted_files: SortedList[tuple[int, int]] = SortedList()

    def upload_file(self, file_id: int) -> None:
        """
        Uploads a new file with initial popularity 0.

        Args:
            file_id: The unique identifier for the file.
        """
        if file_id in self.file_to_popularity:
            return
        
        self.file_to_popularity[file_id] = 0
        # Store as (-popularity, file_id) for natural ascending sort
        # which results in (highest popularity, lowest ID)
        self.sorted_files.add((0, file_id))

    def view_file(self, file_id: int) -> int:
        """
        Increments the popularity of a file and returns the new popularity.

        Args:
            file_id: The unique identifier for the file.

        Returns:
            The updated popularity of the file.
        """
        if file_id not in self.file_to_popularity:
            return -1
        
        old_popularity = self.file_to_popularity[file_id]
        new_popularity = old_popularity + 1
        
        # Remove old entry from sorted structure to update it
        self.sorted_files.remove((-old_popularity, file_id))
        
        # Update map and re-insert into sorted structure
        self.file_to_popularity[file_id] = new_popularity
        self.sorted_files.add((-new_popularity, file_id))
        
        return new_popularity

    def get_trending_file(self) -> int:
        """
        Retrieves the most popular file. If ties exist, returns the one with the smallest ID.

        Returns:
            The file_id of the trending file, or -1 if no files exist.
        """
        if not self.sorted_files:
            return -1
        
        # The first element in SortedList is the smallest tuple.
        # Since we store (-popularity, file_id), the smallest tuple 
        # corresponds to the highest popularity and then the smallest ID.
        _, file_id = self.sorted_files[0]
        return file_id

    def delete_file(self, file_id: int) -> bool:
        """
        Deletes a file from the system.

        Args:
            file_id: The unique identifier for the file.

        Returns:
            True if the file was deleted, False if it didn't exist.
        """
        if file_id not in self.file_to_popularity:
            return False
        
        popularity = self.file_to_popularity[file_id]
        # Remove from both the lookup map and the sorted structure
        self.sorted_files.remove((-popularity, file_id))
        del self.file_to_popularity[file_id]
        return True

def solve():
    """
    Example usage of the FileSharingSystem.
    """
    system = FileSharingSystem()
    
    # Test Upload
    system.upload_file(1)
    system.upload_file(2)
    system.upload_file(3)
    
    # Test View (Popularity increment)
    print(f"View 1: {system.view_file(1)}") # Expected: 1
    print(f"View 2: {system.view_file(2)}") # Expected: 1
    print(f"View 1: {system.view_file(1)}") # Expected: 2
    
    # Test Trending
    # File 1 has popularity 2, File 2 has 1, File 3 has 0.
    print(f"Trending: {system.get_trending_file()}") # Expected: 1
    
    # Test Tie-breaking
    # Upload file 4, view it once. Now 1 and 4 both have popularity 1 (if 1 was reset)
    # Let's make 2 and 4 have same popularity.
    system.upload_file(4)
    system.view_file(4) # 4 has popularity 1
    system.view_file(2) # 2 has popularity 2
    # Current: 1(2), 2(2), 4(1), 3(0)
    # Tie between 1 and 2. Smallest ID is 1.
    print(f"Trending (Tie 1 vs 2): {system.get_trending_file()}") # Expected: 1
    
    # Test Delete
    system.delete_file(1)
    print(f"Trending after deleting 1: {system.get_trending_file()}") # Expected: 2
