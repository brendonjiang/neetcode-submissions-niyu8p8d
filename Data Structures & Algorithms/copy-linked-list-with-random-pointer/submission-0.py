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
        myMap = {}
    
        
        def list_traversal(node):
            if not node:
                return None
            if node in myMap:
                return myMap[node]

            copy = Node(node.val)
            myMap[node] = copy

            copy.next = list_traversal(node.next)
            copy.random = list_traversal(node.random)

            return copy
        

        return list_traversal(head) if head else None

            
