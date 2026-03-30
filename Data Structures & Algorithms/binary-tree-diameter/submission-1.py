# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def max_depth(root):
            if not root:
                return 0

            depth = 1
            depth_left = max_depth(root.left)
            depth_right = max_depth(root.right)
            
            self.res = max(self.res, depth_left + depth_right)
            return depth + max(depth_left, depth_right)

        
        max_depth(root)

        return self.res

        