# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def diameter1(root):
            nonlocal diameter

            if not root:
                return 0

            depth = 1

            depthL = diameter1(root.left)
            depthR = diameter1(root.right)

            diameter = max(diameter, depthL+depthR)

            return depth + max(depthL, depthR)


        diameter1(root)
        return diameter