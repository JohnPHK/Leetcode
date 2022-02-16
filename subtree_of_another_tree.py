# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equalTree(t1, t2):
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            else:
                return t1.val == t2.val and equalTree(t1.left, t2.left) and equalTree(t1.right, t2.right)
            
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        else:
            return equalTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)