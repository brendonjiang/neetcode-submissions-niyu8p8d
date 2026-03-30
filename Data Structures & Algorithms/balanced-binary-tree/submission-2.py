# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            nonlocal isBalanced
            if not node:
                return 0

            depth = 1

            depthL = dfs(node.left)
            depthR = dfs(node.right)

            if abs(depthL - depthR) > 1:
                isBalanced = False

            return depth + max(depthL, depthR)

        isBalanced = True

        dfs(root)
        return isBalanced