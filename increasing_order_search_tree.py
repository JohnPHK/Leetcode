# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tail = TreeNode()
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = self.tail
        def inorderTraversal(node):
            if node is not None:
                inorderTraversal(node.left)
                self.tail.right = node
                self.tail = self.tail.right
                self.tail.left = None
                
                inorderTraversal(node.right)
        
        inorderTraversal(root)
        
        return dummy.right
            