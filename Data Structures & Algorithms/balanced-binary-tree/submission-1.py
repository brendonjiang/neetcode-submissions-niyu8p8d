# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isBalan = True

        def height(root):
            nonlocal isBalan
            if not root:
                return 0

            depth = 1

            depthL = height(root.left)
            depthR = height(root.right)

            if abs(depthL - depthR) > 1:
                isBalan = False

            return depth + max(depthL, depthR)

        height(root)
        return isBalan