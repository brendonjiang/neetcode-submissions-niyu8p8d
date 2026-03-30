"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        myCache = {}

        def dfs(node):
            if not node:
                return None

            if node in myCache:
                return myCache[node]

            copy = Node(node.val)
            myCache[node] = copy
            copy.next = dfs(node.next)
            copy.random = dfs(node.random)

            

            return myCache[node]


        return dfs(head)