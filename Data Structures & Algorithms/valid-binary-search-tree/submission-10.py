# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True

        def dfs(root, lower, upper):
            if not root:
                return

            if lower >= root.val or root.val >= upper:
                nonlocal isValid
                isValid = False
                return
            
            dfs(root.left, lower, root.val)
            dfs(root.right, root.val, upper)

            return 

        dfs(root, float("-inf"), float("inf"))

        return isValid 
        