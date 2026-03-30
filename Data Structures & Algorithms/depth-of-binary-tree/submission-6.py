# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        q = deque()

        if not root:
            return 0

        q.append(root)
        depth = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

                
            depth += 1

        return depth