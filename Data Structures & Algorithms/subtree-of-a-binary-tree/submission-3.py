# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        target = subRoot.val

        def isSame(p, q):
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)

            else:
                return False

        self.subtree = False

        def find_node(root):
            if not root:
                return

            if root.val == target:
                self.subtree = isSame(root, subRoot)
                if self.subtree:
                    return
                    
                


            
            find_node(root.left)
            find_node(root.right)

        find_node(root)
        return self.subtree
