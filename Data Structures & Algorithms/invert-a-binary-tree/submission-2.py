# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        if not root:
            return root

        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            for i in range(len(queue)):
                cur = queue.popleft()
                
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)

                cur.left, cur.right = cur.right, cur.left

        return root