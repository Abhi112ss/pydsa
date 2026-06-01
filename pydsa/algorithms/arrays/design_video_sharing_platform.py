METADATA = {
    "id": 2254,
    "name": "Design Video Sharing Platform",
    "slug": "design-video-sharing-platform",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "simulation", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a system to manage video metadata, view counts, and user interactions with O(1) complexity.",
}

class VideoSharingPlatform:
    """
    A system to manage video metadata and view counts.
    
    Attributes:
        video_metadata (dict[int, str]): Maps video_id to video_title.
        video_views (dict[int, int]): Maps video_id to view_count.
    """

    def __init__(self) -> None:
        """Initializes the platform with empty storage."""
        self.video_metadata: dict[int, str] = {}
        self.video_views: dict[int, int] = {}

    def upload_video(self, video_id: int, title: str) -> None:
        """
        Uploads a new video to the platform.

        Args:
            video_id (int): The unique identifier for the video.
            title (str): The title of the video.
        """
        # Store metadata and initialize view count to 0
        self.video_metadata[video_id] = title
        self.video_views[video_id] = 0

    def watch_video(self, video_id: int) -> None:
        """
        Increments the view count for a specific video.

        Args:
            video_id (int): The unique identifier for the video.
        """
        # Increment view count if video exists
        if video_id in self.video_views:
            self.video_views[video_id] += 1

    def get_video_title(self, video_id: int) -> str:
        """
        Retrieves the title of a video.

        Args:
            video_id (int): The unique identifier for the video.

        Returns:
            str: The title of the video, or an empty string if not found.
        """
        return self.video_metadata.get(video_id, "")

    def get_view_count(self, video_id: int) -> int:
        """
        Retrieves the number of views for a video.

        Args:
            video_id (int): The unique identifier for the video.

        Returns:
            int: The view count, or 0 if the video does not exist.
        """
        return self.video_views.get(video_id, 0)


def solve() -> None:
    """
    Example usage of the VideoSharingPlatform.
    """
    platform = VideoSharingPlatform()
    
    # Test Upload
    platform.upload_video(1, "Python Tutorial")
    platform.upload_video(2, "Algorithm Design")
    
    # Test Watch
    platform.watch_video(1)
    platform.watch_video(1)
    platform.watch_video(2)
    
    # Test Get Title
    assert platform.get_video_title(1) == "Python Tutorial"
    assert platform.get_video_title(3) == ""
    
    # Test Get Views
    assert platform.get_view_count(1) == 2
    assert platform.get_view_count(2) == 1
    assert platform.get_view_count(3) == 0

    print("All tests passed!")
