# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def returnAllElements(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        elif root.left is None:
            return [root.val] + self.returnAllElements(root.right)
        elif root.right is None:
            return  self.returnAllElements(root.left) + [root.val]
        else:
            return self.returnAllElements(root.left) + [root.val] + self.returnAllElements(root.right)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        all_elements = self.returnAllElements(root1) + self.returnAllElements(root2)
        all_elements.sort()
        return all_elements
