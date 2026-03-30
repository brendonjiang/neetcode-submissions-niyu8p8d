# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def dfs(root, target):
            if not root:
                return
            
            if root.val >= target:
                nonlocal count
                count += 1
            
            target = max(root.val, target)


            dfs(root.left, target)
            dfs(root.right, target)

            return

        dfs(root, float("-inf"))

        return count

