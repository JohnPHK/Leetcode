# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return
        
        if high >= root.val and root.val >= low:
            print("hello", root.val)
            trimmed = TreeNode(root.val, self.trimBST(root.left, low, high), self.trimBST(root.right, low, high))
        elif root.val < low:
            trimmed = self.trimBST(root.right, low, high)
        else:
            trimmed = self.trimBST(root.left, low, high)
        
        return trimmed