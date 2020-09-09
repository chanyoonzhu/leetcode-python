# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        """
        - dfs
        - O(n + e)
        - O(n)
        """
        visited = set()
        host_name = startUrl.split("/")[2]
        res = []
        
        def is_same_host(url):
            return url.split("/")[2] == host_name
            
        def dfs(url):
            res.append(url)
            visited.add(url)
            links = htmlParser.getUrls(url)
            for link in links:
                if link not in visited and is_same_host(link):
                    dfs(link)
        
        dfs(startUrl)
        return res

        """
        - bfs, did not figure out why couldn't work
        - O(n + e)
        - O(n)
        """
        def get_host_name(url):
            return url.split("/")[2]
        
        visited = set(startUrl)
        host_name = get_host_name(startUrl)
        queue = [startUrl]
            
        while queue:
            url = queue.pop(0)
            for link in htmlParser.getUrls(url):
                if link not in visited and get_host_name(link) == host_name:
                    queue.append(link)
                    visited.add(link)
        return list(visited)
        