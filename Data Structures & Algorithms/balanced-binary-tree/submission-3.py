# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            
            if not node:
                return [True, 0]

            depth = 1

            depthL = dfs(node.left)
            depthR = dfs(node.right)

            if depthL[0] and depthR[0] and abs(depthL[1] - depthR[1]) <= 1:
                return [True, depth + max(depthL[1], depthR[1])]

            else:
                return [False, depth + max(depthL[1], depthR[1])]


        
        return dfs(root)[0]