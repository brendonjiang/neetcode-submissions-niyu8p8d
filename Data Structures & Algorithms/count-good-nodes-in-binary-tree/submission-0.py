# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root, max_value):
            count = 0

            if not root:
                return count
            
            if root.val >= max_value:
                count = 1

            max_value = max(max_value, root.val)

            count += dfs(root.left, max_value)
            count += dfs(root.right, max_value)


            return count

        
        return dfs(root, float("-inf"))