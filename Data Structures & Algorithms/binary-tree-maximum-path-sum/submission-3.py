# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def dfs(node):
            nonlocal max_path

            if not node:
                return 0

            left_max = dfs(node.left)
            right_max = dfs(node.right)

            if left_max < 0:
                left_max = 0

            if right_max < 0:
                right_max = 0
                
            non_split = node.val + left_max + right_max
            max_path = max(max_path, non_split)
            max_path = max(max_path, node.val)

            return node.val + max(left_max, right_max)
            
        dfs(root)
        return max_path