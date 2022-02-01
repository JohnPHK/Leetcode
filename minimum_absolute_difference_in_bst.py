# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.diff = 10**6
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            if self.prev is not None:
                self.diff = min(self.diff, abs(root.val - self.prev.val))
            self.prev = root
            inorder(root.right)
        
        inorder(root)
        return self.diff
            