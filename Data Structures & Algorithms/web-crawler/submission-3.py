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
        
        output = []
        visits = set()
        
        name = []
        count = 0
        for char in startUrl:
            if char == "/":
                count += 1
            

            if count == 3:
                break

            name.append(char)
        host_name = "".join(name)
            
        from collections import deque

        q = deque()
        q.append(startUrl)

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                output.append(cur)
                visits.add(cur)

                links = htmlParser.getUrls(cur)

                for link in links:
                    if host_name in link and link not in visits:
                        visits.add(link)
                        q.append(link)

        return output

