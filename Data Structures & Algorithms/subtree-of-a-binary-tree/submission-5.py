# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            if not root1 and not root2:
                return True

            if (not root1 and root2) or (root1 and not root2) or root1.val != root2.val:
                return False

            return same(root1.left, root2.left) and same(root1.right, root2.right)

        if not root:
            return

        if root.val == subRoot.val:
            if same(root, subRoot):
                return True

        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) or False
        
        