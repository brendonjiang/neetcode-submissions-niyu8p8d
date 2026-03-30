# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def helper(root, output):
            if not root:
                return output

            helper(root.left, output)
            helper(root.right, output)
            output.append(root.val)

            return output


        return helper(root, output)