# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def helper(root, output):
            if not root:
                return output

            output.append(root.val)
            helper(root.left, output)
            helper(root.right, output)
            return output
        return helper(root, output)