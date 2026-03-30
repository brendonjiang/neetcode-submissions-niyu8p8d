# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque()
        queue2 = deque()
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False

        queue1.append(p)
        queue2.append(q)

        while len(queue1) > 0:
            for i in range(len(queue1)):
                curr1 = queue1.popleft()
                curr2 = queue2.popleft()
                
                if curr1.val != curr2.val:
                    return False
                
                if curr1.left and curr2.left:
                    queue1.append(curr1.left)
                    queue2.append(curr2.left)

                
                    

                if curr1.right and curr2.right:
                    queue1.append(curr1.right)
                    queue2.append(curr2.right)
                
                if (not curr1.left and curr2.left) or (curr1.left and not curr2.left) or (not curr1.right and curr2.right) or (curr1.right and not curr2.right):
                    return False


                    

            
        return True