METADATA = {
    "id": 1236,
    "name": "Web Crawler",
    "slug": "web-crawler",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "graph", "queue"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Implement a web crawler that explores URLs starting from a root URL, staying within the same hostname.",
}

from collections import deque

class HtmlParser:
    """
    A mock class provided by the problem description.
    """
    def getUrls(self, url: str) -> list[str]:
        # This is a placeholder for the actual implementation provided by LeetCode
        return []

class Solution:
    def crawl(self, startUrl: str, htmlParser: HtmlParser) -> list[str]:
        """
        Crawls the web starting from startUrl, staying within the same hostname.

        Args:
            startUrl: The initial URL to start crawling from.
            htmlParser: An object with a getUrls method to fetch URLs from a page.

        Returns:
            A list of all unique URLs found that belong to the same hostname as startUrl.

        Examples:
            >>> parser = MockHtmlParser()
            >>> sol = Solution()
            >>> sol.crawl("http://news.yahoo.com/news", parser)
            ["http://news.yahoo.com/news", "http://news.yahoo.com/news/1", ...]
        """
        # Extract the hostname from the startUrl
        # Format: http://hostname/path...
        hostname = startUrl.split('/')[2]
        
        # Use a set for O(1) lookup to track visited URLs and prevent infinite loops
        visited = {startUrl}
        
        # Use a queue for Breadth-First Search (BFS) traversal
        queue = deque([startUrl])
        
        while queue:
            current_url = queue.popleft()
            
            # Fetch all URLs linked from the current page
            try:
                neighbor_urls = htmlParser.getUrls(current_url)
            except Exception:
                # In a real-world scenario, we'd handle network errors here
                continue

            for url in neighbor_urls:
                # Check if the URL belongs to the same hostname and hasn't been visited
                # We split by '/' and check the 2nd index (the hostname)
                if url.split('/')[2] == hostname and url not in visited:
                    visited.add(url)
                    queue.append(url)
                    
        return list(visited)

def solve():
    """
    Example usage of the Solution class.
    """
    class MockHtmlParser(HtmlParser):
        def getUrls(self, url: str) -> list[str]:
            mapping = {
                "http://news.yahoo.com/news": ["http://news.yahoo.com/news/1", "http://google.com"],
                "http://news.yahoo.com/news/1": ["http://news.yahoo.com/news/2"],
                "http://news.yahoo.com/news/2": ["http://news.yahoo.com/news"],
            }
            return mapping.get(url, [])

    start_url = "http://news.yahoo.com/news"
    parser = MockHtmlParser()
    solution = Solution()
    result = solution.crawl(start_url, parser)
    print(f"Crawled URLs: {result}")
