# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.isBalanced = True

        def depth(root):
            if not root:
                return 0

            height = 1

            depthL = depth(root.left)
            depthR = depth(root.right)

            if abs(depthL - depthR) > 1:
                self.isBalanced = False

            return (height + max(depthL, depthR))

        depth(root)

        return self.isBalanced

        
        