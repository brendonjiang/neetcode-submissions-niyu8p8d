# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, targetSum, total):

            if not root:
                return False

            total += root.val

            if not root.left and not root.right:
                return total == targetSum

            
            return (helper(root.left, targetSum, total) or helper(root.right, targetSum, total))

        return helper(root, targetSum, 0)