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
            
        def dfs(url, visits, host_name):
            output.append(url)
            visits.add(url)

            connections = htmlParser.getUrls(url)
            

            for link in connections:
                if host_name in link and link not in visits:
                    dfs(link, visits, host_name)

            return output

        
        return dfs(startUrl, visits, host_name)

