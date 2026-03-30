# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root
        queue = deque()
        output = root
        queue.append(root)
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)

                if curr.left:
                    queue.append(curr.left)

                curr.left, curr.right = curr.right, curr.left

        return output


        


        